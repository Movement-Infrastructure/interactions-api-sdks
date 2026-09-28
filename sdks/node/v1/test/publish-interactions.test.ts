// POST /v1/interactions against a mocked server.
//
// The spec defines no operationId for the interactions endpoints, so the
// generator derives the method name from the path and verb, giving
// `vversionInteractionsPost`. `version` is a required request field -- the
// client does not default it -- so the path only resolves to /v1/interactions
// because the caller passes "1".

import { http, HttpResponse } from 'msw';
import { setupServer } from 'msw/node';
import { afterAll, afterEach, beforeAll, describe, expect, it } from 'vitest';

import {
  Configuration,
  ContactMethod,
  InteractionsApi,
  Outcome,
  type InteractionsDto,
} from '../src/index';

const HOST = 'http://localhost:4010';
const API_VERSION = '1';
const API_KEY = 'test';

// Minimal request the API accepts.
const REQUEST_BODY: InteractionsDto = {
  interactions: [
    {
      stateCode: 'CA',
      attemptDateTime: new Date('2026-07-30T10:00:00Z'),
      method: ContactMethod.PhoneCall,
      committee: [{ type: 'Matchbook', id: '1' }],
      vendorSource: 'Matchbook',
      outcome: Outcome.SuccessfulContact,
    },
  ],
};

const MOCK_RESPONSE = {
  correlationId: 'test-correlation-123',
  totalInteractions: 1,
  acceptedInteractions: {
    count: 1,
    data: [{ interactionId: '11111111-1111-1111-1111-111111111111', index: 0 }],
  },
  rejectedInteractions: { count: 0, data: [] },
};

const server = setupServer();

// `error` rather than the default warn: a request to an unexpected path is the
// exact failure this suite exists to catch, so it must fail the test.
beforeAll(() => server.listen({ onUnhandledRequest: 'error' }));
afterEach(() => server.resetHandlers());
afterAll(() => server.close());

function client(): InteractionsApi {
  return new InteractionsApi(
    new Configuration({
      basePath: HOST,
      // The endpoint is behind HTTP basic auth with the API key in the password
      // field and an empty username. The mock ignores it, but setting
      // credentials exercises the client's auth path.
      username: '',
      password: API_KEY,
    }),
  );
}

describe('InteractionsApi', () => {
  it('posts interactions and deserializes the batch result', async () => {
    server.use(
      http.post(`${HOST}/v1/interactions`, () => HttpResponse.json(MOCK_RESPONSE)),
    );

    const result = await client().vversionInteractionsPost({
      version: API_VERSION,
      interactionsDto: REQUEST_BODY,
    });

    expect(result?.totalInteractions).toBe(1);
    expect(result?.correlationId).toBe('test-correlation-123');
    expect(result?.acceptedInteractions?.count).toBe(1);
  });

  it('resolves the templated path to /v1/ rather than a literal /v{version}/', async () => {
    let requestedPath: string | undefined;

    server.use(
      http.post(`${HOST}/*`, ({ request }) => {
        requestedPath = new URL(request.url).pathname;
        return HttpResponse.json(MOCK_RESPONSE);
      }),
    );

    await client().vversionInteractionsPost({
      version: API_VERSION,
      interactionsDto: REQUEST_BODY,
    });

    expect(requestedPath).toBe('/v1/interactions');
    expect(requestedPath).not.toContain('%7Bversion%7D');
  });

  it('sends the API key as basic auth with an empty username', async () => {
    let authorization: string | null = null;

    server.use(
      http.post(`${HOST}/v1/interactions`, ({ request }) => {
        authorization = request.headers.get('Authorization');
        return HttpResponse.json(MOCK_RESPONSE);
      }),
    );

    await client().vversionInteractionsPost({
      version: API_VERSION,
      interactionsDto: REQUEST_BODY,
    });

    expect(authorization).toBe(`Basic ${btoa(`:${API_KEY}`)}`);
  });

  it('serializes the interaction body the API expects', async () => {
    let body: any;

    server.use(
      http.post(`${HOST}/v1/interactions`, async ({ request }) => {
        body = await request.json();
        return HttpResponse.json(MOCK_RESPONSE);
      }),
    );

    await client().vversionInteractionsPost({
      version: API_VERSION,
      interactionsDto: REQUEST_BODY,
    });

    expect(body.interactions).toHaveLength(1);
    expect(body.interactions[0].stateCode).toBe('CA');
    expect(body.interactions[0].method).toBe('phone_call');
    expect(body.interactions[0].outcome).toBe('successful_contact');
    // Dates cross the wire as ISO 8601, not as a JS Date.
    expect(body.interactions[0].attemptDateTime).toBe('2026-07-30T10:00:00.000Z');
  });
});
