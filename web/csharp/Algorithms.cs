namespace PolyglotLive;

public static class Algorithms
{
    public static int Solve(string task, int a, int b = 0)
    {
        int maximum = task switch { "factorial" => 12, "fibonacci" => 30, _ => 1000000 };
        if (a < 0 || a > maximum || (task == "gcd" && (b < 0 || b > 1000000)))
            throw new ArgumentOutOfRangeException(nameof(a), "Input outside the documented domain.");
        switch (task)
        {
            case "gcd":
                while (b != 0) { int remainder = a % b; a = b; b = remainder; }
                return a;
            case "factorial":
                int product = 1;
                for (int i = 2; i <= a; i++) product = checked(product * i);
                return product;
            case "prime":
                if (a < 2) return 0;
                for (int d = 2; d <= a / d; d++) if (a % d == 0) return 0;
                return 1;
            case "fibonacci":
                int previous = 0, current = 1;
                for (int i = 0; i < a; i++)
                {
                    int next = checked(previous + current);
                    previous = current;
                    current = next;
                }
                return previous;
            default: throw new ArgumentException("Unknown algorithm.");
        }
    }
}
