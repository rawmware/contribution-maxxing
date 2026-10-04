def solve(n)
  return 0 if n < 2
  d = 2
  while d * d <= n
    return 0 if n % d == 0
    d += 1
  end
  1
end

puts solve(0)
puts solve(1)
puts solve(2)
puts solve(3)
puts solve(4)
puts solve(25)
puts solve(97)
puts solve(121)
puts solve(997)
