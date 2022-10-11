def solve(n):
    if n == 1 or n == 3: return -1
    res = []
    if n % 2 == 0:
        res = map(str, reversed(range(1, n + 1)))
    else:
        res = list(range(n, n//2 + 1, -1)) + list(range(1, n//2 + 2))
        res = map(str, res)
    return " ".join(res)



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(solve(n))