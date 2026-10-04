def solve(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    print(solve(0, 0))
    print(solve(0, 7))
    print(solve(7, 0))
    print(solve(48, 18))
    print(solve(17, 13))
    print(solve(270, 192))
