# ddxinteractionsapi

Go client for the DDx Interactions API, generated from its OpenAPI
specification.

- API version: v1
- Package version: 0.1.0
- Generator version: 7.10.0

## Requirements

Go 1.22 or later.

## Installation

```shell
go get github.com/Movement-Infrastructure/interactions-api-sdks/sdks/go@latest
```

```go
import "github.com/Movement-Infrastructure/interactions-api-sdks/sdks/go"
```

## Changelog

API changes are recorded in the
[changelog](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/go/CHANGELOG.md),
regenerated from a diff of the OpenAPI specification on each sync. Entries
marked **breaking** require a change on the consumer side.

## Reporting issues

This package is generated. Edits to it are overwritten on the next spec sync.
Report problems against the API specification rather than the generated code.

## Getting Started

```go
package main

import (
	"context"
	"errors"
	"fmt"
	"log"
	"os"

	"github.com/Movement-Infrastructure/interactions-api-sdks/sdks/go"
)

func main() {
	client := ddxinteractionsapi.NewAPIClient(ddxinteractionsapi.NewConfiguration())

	// HTTP basic auth, API key in the password field, empty username.
	// The client already defaults to the production API.
	ctx := context.WithValue(context.Background(), ddxinteractionsapi.ContextBasicAuth, ddxinteractionsapi.BasicAuth{
		UserName: "",
		Password: os.Getenv("DDX_API_KEY"),
	})

	me, _, err := client.AuthenticationDetailsAPI.VversionAuthMeGet(ctx, "1").Execute()
	if err != nil {
		// The error string carries only the status line. The body says why.
		var apiErr *ddxinteractionsapi.GenericOpenAPIError
		if errors.As(err, &apiErr) {
			log.Fatalf("Interactions API returned %s: %s", apiErr.Error(), apiErr.Body())
		}
		log.Fatal(err)
	}
	fmt.Println(me)
}
```

Model fields are pointers so that an unset field can be told apart from a zero
value. The `PtrString`, `PtrInt32`, `PtrBool` and `PtrTime` helpers build them
inline.

## Documentation

Per-endpoint and per-model pages are generated alongside the client in
[docs](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/go/docs).
The same field documentation is on [pkg.go.dev](https://pkg.go.dev/github.com/Movement-Infrastructure/interactions-api-sdks/sdks/go).
