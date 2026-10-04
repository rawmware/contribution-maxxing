local function solve(n)
  local a, b = 0, 1
  for i = 1, n do a, b = b, a + b end
  return a
end

print(string.format("%.0f", solve(0)))
print(string.format("%.0f", solve(1)))
print(string.format("%.0f", solve(2)))
print(string.format("%.0f", solve(3)))
print(string.format("%.0f", solve(10)))
print(string.format("%.0f", solve(20)))
print(string.format("%.0f", solve(30)))
