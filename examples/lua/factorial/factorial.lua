local function solve(n)
  local r = 1
  for i = 2, n do r = r * i end
  return r
end

print(string.format("%.0f", solve(0)))
print(string.format("%.0f", solve(1)))
print(string.format("%.0f", solve(2)))
print(string.format("%.0f", solve(5)))
print(string.format("%.0f", solve(10)))
print(string.format("%.0f", solve(12)))
