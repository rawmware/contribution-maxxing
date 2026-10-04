local function solve(a, b)
  while b ~= 0 do a, b = b, a % b end
  return a
end

print(string.format("%.0f", solve(0, 0)))
print(string.format("%.0f", solve(0, 7)))
print(string.format("%.0f", solve(7, 0)))
print(string.format("%.0f", solve(48, 18)))
print(string.format("%.0f", solve(17, 13)))
print(string.format("%.0f", solve(270, 192)))
