using System.Text.Json;
using PolyglotLive;

using var document = JsonDocument.Parse(File.ReadAllText(args[0]));
int count = 0;
foreach (var task in document.RootElement.EnumerateObject())
{
    var expected = task.Value.GetProperty("expected").EnumerateArray().ToArray();
    int index = 0;
    foreach (var input in task.Value.GetProperty("cases").EnumerateArray())
    {
        var values = input.EnumerateArray().Select(v => v.GetInt32()).ToArray();
        int actual = Algorithms.Solve(task.Name, values[0], values.Length > 1 ? values[1] : 0);
        if (actual != expected[index++].GetInt32()) throw new Exception($"Mismatch: {task.Name}");
        count++;
    }
}
Console.WriteLine($"PASS C# browser algorithm sources: {count} shared cases");
