for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    res = "YES"
    up = False
    for i in range(n - 1):
        if a[i] < a[i + 1]:
            up = True 
        elif a[i] > a[i + 1] and up:
            res = "NO"
            break
    print(res)


