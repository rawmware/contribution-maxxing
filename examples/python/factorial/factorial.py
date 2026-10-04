def solve(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    print(solve(0))
    print(solve(1))
    print(solve(2))
    print(solve(5))
    print(solve(10))
    print(solve(12))
