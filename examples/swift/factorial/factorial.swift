func solve(_ n: Int) -> Int { var r = 1; if n >= 2 { for i in 2...n { r *= i } }; return r }

print(solve(0))
print(solve(1))
print(solve(2))
print(solve(5))
print(solve(10))
print(solve(12))
