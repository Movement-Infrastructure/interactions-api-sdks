// Checks the generated client compiles and exposes the surface consumers depend
// on, without the mock server the happy-path tests need.
//
// The names stay stable across regenerations. Services come from the spec's
// tags ("Interactions", "Authentication Details") and models from its
// component schema names.
package test

import (
	"testing"

	"github.com/Movement-Infrastructure/interactions-api-sdks/sdks/go"
)

func TestClientExposesBothAPIServices(t *testing.T) {
	client := ddxinteractionsapi.NewAPIClient(ddxinteractionsapi.NewConfiguration())

	if client.InteractionsAPI == nil {
		t.Fatal("InteractionsAPI is nil; the Interactions tag did not generate a service")
	}
	if client.AuthenticationDetailsAPI == nil {
		t.Fatal("AuthenticationDetailsAPI is nil; the Authentication Details tag did not generate a service")
	}
}

func TestDefaultsToTheProductionHost(t *testing.T) {
	// Index 0 of the spec's servers block is what a client uses unless the
	// caller picks another.
	url, err := ddxinteractionsapi.NewConfiguration().ServerURL(0, nil)
	if err != nil {
		t.Fatalf("ServerURL(0): %v", err)
	}
	if url != "https://api.movementinfrastructure.org" {
		t.Fatalf("default server is %q, want the production host", url)
	}
}

func TestTakesAServerOverride(t *testing.T) {
	cfg := ddxinteractionsapi.NewConfiguration()
	cfg.Servers = ddxinteractionsapi.ServerConfigurations{{URL: "http://localhost:4010"}}

	url, err := cfg.ServerURL(0, nil)
	if err != nil {
		t.Fatalf("ServerURL(0): %v", err)
	}
	if url != "http://localhost:4010" {
		t.Fatalf("server override not applied; got %q", url)
	}
}

func TestEnumConstantsArePrefixedWithTheirType(t *testing.T) {
	// Without enumClassPrefix the UNKNOWN members collide and the package does
	// not compile. This test mostly records why the option is set.
	if ddxinteractionsapi.OUTCOME_UNKNOWN != "unknown" || ddxinteractionsapi.CONTACTMETHOD_UNKNOWN != "unknown" {
		t.Fatal("prefixed enum constants have unexpected values")
	}
}
