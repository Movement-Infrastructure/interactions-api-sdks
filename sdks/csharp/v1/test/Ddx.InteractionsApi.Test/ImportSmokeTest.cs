using System.Text.RegularExpressions;
using Ddx.InteractionsApi.Api;
using Ddx.InteractionsApi.Client;
using Ddx.InteractionsApi.Model;
using Xunit;

namespace InteractionsApiSdkTests;

/// <summary>
/// Proves the generated assembly builds and exposes the surface consumers
/// depend on. Cheap to run and catches a broken generation before the
/// happy-path test has to stand up a stubbed transport.
///
/// These names are stable across regenerations: the API classes come from the
/// spec's tags ("Interactions", "Authentication Details") and the models from
/// the component schema names.
/// </summary>
public class ImportSmokeTest
{
    [Fact]
    public void ExposesTheCoreClientTypes()
    {
        Assert.NotNull(typeof(ApiClient));
        Assert.NotNull(typeof(Configuration));
        Assert.NotNull(typeof(ApiException));
    }

    [Fact]
    public void ExposesTheApiClasses()
    {
        Assert.NotNull(typeof(InteractionsApi));
        Assert.NotNull(typeof(AuthenticationDetailsApi));
    }

    [Fact]
    public void ExposesTheModelsTheHappyPathRoundTrips()
    {
        Assert.NotNull(typeof(InteractionsDto));
        Assert.NotNull(typeof(InteractionsBatchResultDto));
        Assert.NotNull(typeof(WhoAmIApiKeyDto));
    }

    [Fact]
    public void ReportsTheVersionTheGeneratorConfigSet()
    {
        // Tracks packageVersion in openapi-generator-config.yaml, which the
        // version-bump workflow rewrites on each sync PR.
        Assert.Matches(new Regex(@"^\d+\.\d+\.\d+"), Configuration.Version);
    }

    [Fact]
    public void DefaultsToTheProductionHost()
    {
        Assert.Equal("https://api.movementinfrastructure.org", new Configuration().BasePath);
    }

    [Fact]
    public void TakesABasePathOverride()
    {
        var config = new Configuration { BasePath = "http://localhost:4010" };
        Assert.Equal("http://localhost:4010", config.BasePath);
    }
}
