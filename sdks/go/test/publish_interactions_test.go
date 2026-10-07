// POST /v1/interactions against a mocked server.
//
// The spec defines no operationId for the interactions endpoints. The generator
// derives VversionInteractionsPost from the path and verb instead. `version` is
// a required argument with no default, and the path resolves to
// /v1/interactions only because the caller passes "1".
package test

import (
	"context"
	"encoding/base64"
	"encoding/json"
	"errors"
	"io"
	"net/http"
	"net/http/httptest"
	"testing"
	"time"

	"github.com/Movement-Infrastructure/interactions-api-sdks/sdks/go"
)

const (
	apiVersion = "1"
	apiKey     = "test"
)

const mockResponse = `{
  "correlationId": "test-correlation-123",
  "totalInteractions": 1,
  "acceptedInteractions": {
    "count": 1,
    "data": [{"interactionId": "11111111-1111-1111-1111-111111111111", "index": 0}]
  },
  "rejectedInteractions": {"count": 0, "data": []}
}`

// capturedRequest is what the mock server saw.
type capturedRequest struct {
	path          string
	authorization string
	body          []byte
}

// newServer answers every request with status and body, recording the request.
func newServer(t *testing.T, status int, body string) (*httptest.Server, *capturedRequest) {
	t.Helper()
	seen := &capturedRequest{}
	srv := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		seen.path = r.URL.EscapedPath()
		seen.authorization = r.Header.Get("Authorization")
		seen.body, _ = io.ReadAll(r.Body)
		w.Header().Set("Content-Type", "application/json")
		w.WriteHeader(status)
		_, _ = io.WriteString(w, body)
	}))
	t.Cleanup(srv.Close)
	return srv, seen
}

func newClient(baseURL string) *ddxinteractionsapi.APIClient {
	cfg := ddxinteractionsapi.NewConfiguration()
	cfg.Servers = ddxinteractionsapi.ServerConfigurations{{URL: baseURL}}
	return ddxinteractionsapi.NewAPIClient(cfg)
}

// authContext carries the API key as basic auth with an empty username.
func authContext() context.Context {
	return context.WithValue(context.Background(), ddxinteractionsapi.ContextBasicAuth, ddxinteractionsapi.BasicAuth{
		UserName: "",
		Password: apiKey,
	})
}

// minimalRequest is the smallest body the API accepts.
func minimalRequest() ddxinteractionsapi.InteractionsDto {
	interaction := ddxinteractionsapi.NewInteractionDto(
		"CA",
		time.Date(2026, 7, 30, 10, 0, 0, 0, time.UTC),
		ddxinteractionsapi.CONTACTMETHOD_PHONE_CALL,
		[]ddxinteractionsapi.CommitteeDetails{*ddxinteractionsapi.NewCommitteeDetails("Matchbook", "1")},
		"Matchbook",
		ddxinteractionsapi.OUTCOME_SUCCESSFUL_CONTACT,
	)
	body := ddxinteractionsapi.NewInteractionsDto()
	body.SetInteractions([]ddxinteractionsapi.InteractionDto{*interaction})
	return *body
}

func post(t *testing.T, baseURL string) (*ddxinteractionsapi.InteractionsBatchResultDto, *http.Response, error) {
	t.Helper()
	return newClient(baseURL).InteractionsAPI.
		VversionInteractionsPost(authContext(), apiVersion).
		InteractionsDto(minimalRequest()).
		Execute()
}

func TestPostsInteractionsAndDeserializesTheBatchResult(t *testing.T) {
	srv, _ := newServer(t, http.StatusOK, mockResponse)

	result, _, err := post(t, srv.URL)
	if err != nil {
		t.Fatalf("VversionInteractionsPost: %v", err)
	}

	if got := result.GetTotalInteractions(); got != 1 {
		t.Errorf("totalInteractions = %d, want 1", got)
	}
	if got := result.GetCorrelationId(); got != "test-correlation-123" {
		t.Errorf("correlationId = %q, want test-correlation-123", got)
	}
	accepted := result.GetAcceptedInteractions()
	if got := accepted.GetCount(); got != 1 {
		t.Errorf("acceptedInteractions.count = %d, want 1", got)
	}
}

func TestResolvesTheTemplatedPathToV1(t *testing.T) {
	srv, seen := newServer(t, http.StatusOK, mockResponse)

	if _, _, err := post(t, srv.URL); err != nil {
		t.Fatalf("VversionInteractionsPost: %v", err)
	}

	if seen.path != "/v1/interactions" {
		t.Fatalf("requested %q, want /v1/interactions rather than a literal /v{version}/", seen.path)
	}
}

func TestSendsTheAPIKeyAsBasicAuthWithAnEmptyUsername(t *testing.T) {
	srv, seen := newServer(t, http.StatusOK, mockResponse)

	if _, _, err := post(t, srv.URL); err != nil {
		t.Fatalf("VversionInteractionsPost: %v", err)
	}

	want := "Basic " + base64.StdEncoding.EncodeToString([]byte(":"+apiKey))
	if seen.authorization != want {
		t.Fatalf("Authorization = %q, want %q", seen.authorization, want)
	}
}

func TestSerializesTheInteractionBodyTheAPIExpects(t *testing.T) {
	srv, seen := newServer(t, http.StatusOK, mockResponse)

	if _, _, err := post(t, srv.URL); err != nil {
		t.Fatalf("VversionInteractionsPost: %v", err)
	}

	var body struct {
		Interactions []map[string]any `json:"interactions"`
	}
	if err := json.Unmarshal(seen.body, &body); err != nil {
		t.Fatalf("request body is not JSON: %v\n%s", err, seen.body)
	}
	if len(body.Interactions) != 1 {
		t.Fatalf("sent %d interactions, want 1", len(body.Interactions))
	}

	sent := body.Interactions[0]
	for field, want := range map[string]string{
		"stateCode": "CA",
		"method":    "phone_call",
		"outcome":   "successful_contact",
		// Dates are sent as RFC 3339 strings.
		"attemptDateTime": "2026-07-30T10:00:00Z",
	} {
		if sent[field] != want {
			t.Errorf("%s = %v, want %q", field, sent[field], want)
		}
	}

	// Several of these are Nullable wrappers, which serialize as null unless
	// the generated MarshalJSON leaves unset ones out.
	for _, field := range []string{"channel", "threadId", "jsonMetadata", "vanFields"} {
		if _, present := sent[field]; present {
			t.Errorf("%s was sent although it was never set", field)
		}
	}
}

func TestSurfacesTheResponseBodyOnAnErrorStatus(t *testing.T) {
	problem := `{"title":"All Interactions Failed Validation","status":400}`
	srv, _ := newServer(t, http.StatusBadRequest, problem)

	_, resp, err := post(t, srv.URL)
	if err == nil {
		t.Fatal("expected an error for a 400 response")
	}
	if resp == nil || resp.StatusCode != http.StatusBadRequest {
		t.Fatalf("response = %v, want status 400", resp)
	}

	var apiErr *ddxinteractionsapi.GenericOpenAPIError
	if !errors.As(err, &apiErr) {
		t.Fatalf("error is %T, want *GenericOpenAPIError so callers can read the body", err)
	}
	if string(apiErr.Body()) != problem {
		t.Fatalf("error body = %q, want the server's problem details", apiErr.Body())
	}
}
