using System.Diagnostics;
using System.Security.Cryptography;
using System.Text.Json;
using System.Text.Json.Nodes;

// Produces a data snapshot, not hundreds of generated HTML source files.
var root = Path.GetFullPath(args.Length > 0 ? args[0] : ".");
var output = Path.Combine(root, ".site");
Directory.CreateDirectory(output);
var languages = new SortedDictionary<string, List<object>>();
var seen = new HashSet<string>();

void AddSource(string language, string task, string relative)
{
    var path = Path.GetFullPath(Path.Combine(root, relative));
    if (!path.StartsWith(root + Path.DirectorySeparatorChar, StringComparison.Ordinal))
        throw new InvalidDataException("Source must stay inside the repository.");
    if (!seen.Add(relative)) return;
    var bytes = File.ReadAllBytes(path);
    if (!languages.TryGetValue(language, out var entries))
        languages[language] = entries = new List<object>();
    entries.Add(new {
        task, source = relative.Replace('\\', '/'), code = File.ReadAllText(path),
        sha256 = Convert.ToHexString(SHA256.HashData(bytes)).ToLowerInvariant()
    });
}

using (var manifest = JsonDocument.Parse(File.ReadAllText(Path.Combine(root, "manifest.json"))))
{
    foreach (var row in manifest.RootElement.EnumerateArray())
        AddSource(row.GetProperty("language").GetString()!, row.GetProperty("task").GetString()!, row.GetProperty("source").GetString()!);
}

foreach (var (language, directory, pattern) in new[] {
    ("Rust", "rust-lab/src", "*.rs"), ("Rust", "web/rust/src", "*.rs"),
    ("C", "examples/c/lab", "*.c"), ("C", "web/c", "*.c"),
    ("CSharp", "web/csharp", "*.cs"), ("CSharp", "web/catalog", "*.cs")
})
{
    foreach (var path in Directory.GetFiles(Path.Combine(root, directory), pattern).Order())
        AddSource(language, Path.GetFileNameWithoutExtension(path), Path.GetRelativePath(root, path));
}

var git = Process.Start(new ProcessStartInfo("git", "rev-parse HEAD") {
    WorkingDirectory = root, RedirectStandardOutput = true, UseShellExecute = false
}) ?? throw new InvalidOperationException("Cannot read repository revision.");
var revision = git.StandardOutput.ReadToEnd().Trim();
git.WaitForExit();
if (git.ExitCode != 0) throw new InvalidOperationException("Cannot read repository revision.");

var data = new {
    languages = languages.Select(pair => new { name = pair.Key, examples = pair.Value }),
    vectors = JsonNode.Parse(File.ReadAllText(Path.Combine(root, "specs/vectors.json"))),
    revision, builtAt = DateTimeOffset.UtcNow.ToString("u")
};
File.WriteAllText(Path.Combine(output, "catalog.json"), JsonSerializer.Serialize(data));
File.WriteAllText(Path.Combine(output, ".nojekyll"), "");
foreach (var asset in new[] { "app.js", "style.css" })
    File.Copy(Path.Combine(root, "web", asset), Path.Combine(output, asset), true);
Console.WriteLine($"Catalog: {languages.Count} languages, {seen.Count} files, one browser application.");
