defmodule Example do
def solve(n), do: fib(n, 0, 1)
defp fib(0, a, _b), do: a
defp fib(n, a, b), do: fib(n - 1, b, a + b)
end

IO.puts(Example.solve(0))
IO.puts(Example.solve(1))
IO.puts(Example.solve(2))
IO.puts(Example.solve(3))
IO.puts(Example.solve(10))
IO.puts(Example.solve(20))
IO.puts(Example.solve(30))
