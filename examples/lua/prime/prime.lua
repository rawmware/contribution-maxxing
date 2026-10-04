local function solve(n)
  if n < 2 then return 0 end
  local d = 2
  while d * d <= n do
    if n % d == 0 then return 0 end
    d = d + 1
  end
  return 1
end

print(string.format("%.0f", solve(0)))
print(string.format("%.0f", solve(1)))
print(string.format("%.0f", solve(2)))
print(string.format("%.0f", solve(3)))
print(string.format("%.0f", solve(4)))
print(string.format("%.0f", solve(25)))
print(string.format("%.0f", solve(97)))
print(string.format("%.0f", solve(121)))
print(string.format("%.0f", solve(997)))
