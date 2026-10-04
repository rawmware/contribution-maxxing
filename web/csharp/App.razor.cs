using Microsoft.AspNetCore.Components;
using Microsoft.JSInterop;
using System.Net.Http.Json;

namespace PolyglotLive;

public partial class App
{
    private Catalog? catalog;
    private Language? selected;
    private string query = "", task = "gcd", inputA = "48", inputB = "18";
    private string loadStatus = "Loading repository source…";
    private string result = "Ready. Choose inputs and run the compiled implementation.";
    private bool busy;
    private readonly Dictionary<string, string> comparisons = new();
    private int Maximum => task switch { "factorial" => 12, "fibonacci" => 30, _ => 1_000_000 };
    private IEnumerable<Language> FilteredLanguages => catalog!.Languages
        .Where(l => (l.DisplayName + " " + l.Name).Contains(query, StringComparison.OrdinalIgnoreCase))
        .OrderBy(l => l.Name switch { "Rust" => 0, "C" => 1, "CSharp" => 2, _ => 3 }).ThenBy(l => l.DisplayName);
    private string RuntimeDescription => selected?.Name switch {
        "Rust" => "Compiled Rust WebAssembly. No JavaScript algorithm substitutes.",
        "C" => "C compiled with Emscripten. Inputs cross a small browser bridge into WebAssembly.",
        _ => "C# running on the same .NET WebAssembly runtime that powers this interface."
    };

    protected override async Task OnInitializedAsync()
    {
        try {
            catalog = await Http.GetFromJsonAsync<Catalog>("catalog.json") ?? throw new Exception("Empty catalog.");
            selected = catalog.Languages.First(l => l.Name == "Rust");
        }
        catch (Exception error) { loadStatus = "Cannot load source catalog. Reload to retry. " + error.Message; }
    }

    private void Select(Language language) {
        selected = language;
        comparisons.Clear();
        result = "Ready. Choose inputs and run the compiled implementation.";
    }

    private void ChangeTask(ChangeEventArgs args) {
        task = args.Value?.ToString() ?? "gcd";
        inputA = task switch { "factorial" => "5", "prime" => "97", "fibonacci" => "10", _ => "48" };
        comparisons.Clear();
        result = "Ready.";
    }

    private (int A, int B) ReadInputs() {
        if (!int.TryParse(inputA, out var a) || a < 0 || a > Maximum)
            throw new ArgumentException($"Input must be a whole number from 0 to {Maximum:N0}.");
        var b = 0;
        if (task == "gcd" && (!int.TryParse(inputB, out b) || b < 0 || b > 1_000_000))
            throw new ArgumentException("Input B must be a whole number from 0 to 1,000,000.");
        return (a, b);
    }

    private async Task<int> Execute(string language, string algorithm, int a, int b) => language == "CSharp"
        ? Algorithms.Solve(algorithm, a, b)
        : await Js.InvokeAsync<int>("polyglot.run", language, algorithm, a, b);

    private async Task Run() {
        busy = true;
        comparisons.Clear();
        try {
            var (a, b) = ReadInputs();
            result = "Loading and executing compiled code…";
            var value = await Execute(selected!.Name, task, a, b);
            result = $"{selected.DisplayName} / {task} → {value}";
        }
        catch (Exception error) { result = "Could not run: " + error.Message; }
        finally { busy = false; }
    }

    private async Task Compare() {
        busy = true;
        comparisons.Clear();
        try {
            var (a, b) = ReadInputs();
            var values = new List<int>();
            foreach (var language in new[] { "Rust", "C", "CSharp" }) {
                try {
                    var value = await Execute(language, task, a, b);
                    values.Add(value);
                    comparisons[language == "CSharp" ? "C#" : language] = value.ToString();
                }
                catch (Exception error) { comparisons[language] = "Unavailable: " + error.Message; }
            }
            result = values.Count == 3 && values.Distinct().Count() == 1
                ? "MATCH / All three compiled implementations agree."
                : "Comparison incomplete or outputs differ. See each runtime result.";
        }
        catch (Exception error) { result = error.Message; }
        finally { busy = false; }
    }

    private async Task Verify() {
        busy = true;
        comparisons.Clear();
        try {
            var passed = 0;
            foreach (var pair in catalog!.Vectors) {
                for (var i = 0; i < pair.Value.Cases.Length; i++) {
                    var input = pair.Value.Cases[i];
                    var actual = await Execute(selected!.Name, pair.Key, input[0], input.Length > 1 ? input[1] : 0);
                    if (actual != pair.Value.Expected[i]) throw new Exception($"{pair.Key} case {i + 1} failed.");
                    passed++;
                }
            }
            result = $"PASS / {passed} shared cases executed in {selected!.DisplayName}.";
        }
        catch (Exception error) { result = "Verification failed: " + error.Message; }
        finally { busy = false; }
    }

    private static string SourceUrl(string path) => "https://github.com/rawmware/contribution-maxxing/blob/main/" + string.Join("/", path.Split('/').Select(Uri.EscapeDataString));
}
