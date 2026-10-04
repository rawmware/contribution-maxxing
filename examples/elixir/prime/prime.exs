defmodule Example do
def solve(n) when n < 2, do: 0
def solve(n), do: trial(n, 2)
defp trial(n, d) when d*d > n, do: 1
defp trial(n, d) do
  if rem(n, d) == 0, do: 0, else: trial(n, d + 1)
end
end

IO.puts(Example.solve(0))
IO.puts(Example.solve(1))
IO.puts(Example.solve(2))
IO.puts(Example.solve(3))
IO.puts(Example.solve(4))
IO.puts(Example.solve(25))
IO.puts(Example.solve(97))
IO.puts(Example.solve(121))
IO.puts(Example.solve(997))
