def solve(arr):
    count = 0
    temp = []
    for s in arr:
        temp.append((s[0] - ord('a') + 1)*31 + (s[1] - ord('a'))*31)
    


if __name__ == "__main__":
    t = int(input())
    res = []
    for _ in range(t):
        n = int(input())
        temp = []
        for _ in range(n):
            temp.append(input())
    res.append(solve(temp))
    print(*res)