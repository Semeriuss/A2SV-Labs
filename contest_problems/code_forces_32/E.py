for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] == a[-1]:
        print(n//2)
    else:
        res = 0
        for i in range(n - 1):
            if a[i] != a[i + 1]:
                res = max(res, (i + 1) * (n - i - 1))
        print(res)