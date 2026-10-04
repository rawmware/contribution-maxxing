def solve(n)
  (2..n).reduce(1) { |r, i| r * i }
end

puts solve(0)
puts solve(1)
puts solve(2)
puts solve(5)
puts solve(10)
puts solve(12)
