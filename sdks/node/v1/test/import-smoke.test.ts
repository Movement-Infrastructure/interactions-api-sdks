// Proves the generated client loads and exposes the surface consumers depend
// on. Cheap to run and catches a broken generation before the happy-path test
// has to stand up a mock server.
//
// These names are stable across regenerations: the API classes come from the
// spec's tags ("Interactions", "Authentication Details") and the models from
// the component schema names.

import { describe, expect, it } from 'vitest';

import {
  AuthenticationDetailsApi,
  BASE_PATH,
  Configuration,
  InteractionsApi,
  InteractionsBatchResultDtoFromJSON,
  InteractionsDtoToJSON,
  ResponseError,
} from '../src/index';

describe('generated client', () => {
  it('exposes the core runtime classes', () => {
    expect(Configuration).toBeTypeOf('function');
    expect(ResponseError).toBeTypeOf('function');
  });

  it('exposes the API classes', () => {
    expect(InteractionsApi).toBeTypeOf('function');
    expect(AuthenticationDetailsApi).toBeTypeOf('function');
  });

  it('exposes the model converters the happy path round-trips', () => {
    expect(InteractionsDtoToJSON).toBeTypeOf('function');
    expect(InteractionsBatchResultDtoFromJSON).toBeTypeOf('function');
  });

  it('defaults to the production host', () => {
    // typescript-fetch bakes in only the spec's first server, so unlike the
    // Ruby and Python clients no non-production host ships in this package.
    expect(BASE_PATH).toBe('https://api.movementinfrastructure.org');
  });

  it('takes a basePath override', () => {
    const config = new Configuration({ basePath: 'http://localhost:4010' });
    expect(config.basePath).toBe('http://localhost:4010');
  });
});
