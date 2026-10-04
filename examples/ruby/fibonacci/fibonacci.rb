def solve(n)
  a, b = 0, 1
  n.times { a, b = b, a + b }
  a
end

puts solve(0)
puts solve(1)
puts solve(2)
puts solve(3)
puts solve(10)
puts solve(20)
puts solve(30)
