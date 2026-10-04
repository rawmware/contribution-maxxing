namespace PolyglotLive;

public sealed class Catalog
{
    public List<Language> Languages { get; set; } = new();
    public Dictionary<string, VectorSet> Vectors { get; set; } = new();
    public string? Revision { get; set; }
    public string BuiltAt { get; set; } = "";
}

public sealed class Language
{
    public string Name { get; set; } = "";
    public List<SourceExample> Examples { get; set; } = new();
    public string DisplayName => Name == "CSharp" ? "C#" : Name;
    public bool IsLive => Name is "Rust" or "C" or "CSharp";
}

public sealed class SourceExample
{
    public string Task { get; set; } = "";
    public string Source { get; set; } = "";
    public string Code { get; set; } = "";
    public string Sha256 { get; set; } = "";
}

public sealed class VectorSet
{
    public string Description { get; set; } = "";
    public int[][] Cases { get; set; } = Array.Empty<int[]>();
    public int[] Expected { get; set; } = Array.Empty<int>();
}
