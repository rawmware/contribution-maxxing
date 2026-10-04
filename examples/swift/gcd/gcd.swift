func solve(_ x: Int, _ y: Int) -> Int { var a = x; var b = y; while b != 0 { (a, b) = (b, a % b) }; return a }

print(solve(0, 0))
print(solve(0, 7))
print(solve(7, 0))
print(solve(48, 18))
print(solve(17, 13))
print(solve(270, 192))
