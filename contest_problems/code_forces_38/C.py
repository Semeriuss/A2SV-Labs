for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    f = list(map(int, input().split()))
    res = [f[0] - s[0]]
    for i in range(1, n):
        if s[i] < f[i - 1]:
            res.append(f[i] - f[i - 1])
        else:
            res.append(f[i] - s[i])
    print(*res)
