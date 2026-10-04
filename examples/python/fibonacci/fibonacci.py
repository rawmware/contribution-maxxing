def solve(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    print(solve(0))
    print(solve(1))
    print(solve(2))
    print(solve(3))
    print(solve(10))
    print(solve(20))
    print(solve(30))
