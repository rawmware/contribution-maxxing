func solve(_ n: Int) -> Int { var a = 0; var b = 1; for _ in 0..<n { (a, b) = (b, a+b) }; return a }

print(solve(0))
print(solve(1))
print(solve(2))
print(solve(3))
print(solve(10))
print(solve(20))
print(solve(30))
