defmodule Example do
def solve(0), do: 1
def solve(n), do: n * solve(n - 1)
end

IO.puts(Example.solve(0))
IO.puts(Example.solve(1))
IO.puts(Example.solve(2))
IO.puts(Example.solve(5))
IO.puts(Example.solve(10))
IO.puts(Example.solve(12))
