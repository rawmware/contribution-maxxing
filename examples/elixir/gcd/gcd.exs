defmodule Example do
def solve(a, 0), do: a
def solve(a, b), do: solve(b, rem(a, b))
end

IO.puts(Example.solve(0, 0))
IO.puts(Example.solve(0, 7))
IO.puts(Example.solve(7, 0))
IO.puts(Example.solve(48, 18))
IO.puts(Example.solve(17, 13))
IO.puts(Example.solve(270, 192))
