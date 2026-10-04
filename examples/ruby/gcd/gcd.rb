def solve(a, b)
  while b != 0
    a, b = b, a % b
  end
  a
end

puts solve(0, 0)
puts solve(0, 7)
puts solve(7, 0)
puts solve(48, 18)
puts solve(17, 13)
puts solve(270, 192)
