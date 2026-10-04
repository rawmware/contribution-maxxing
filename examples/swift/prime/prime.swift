func solve(_ n: Int) -> Int { if n < 2 { return 0 }; var d = 2; while d*d <= n { if n % d == 0 { return 0 }; d += 1 }; return 1 }

print(solve(0))
print(solve(1))
print(solve(2))
print(solve(3))
print(solve(4))
print(solve(25))
print(solve(97))
print(solve(121))
print(solve(997))
