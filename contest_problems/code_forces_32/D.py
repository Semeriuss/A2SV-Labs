def calc(a):
    zeroes = inversions = 0
    for i in range(len(a) - 1, -1, -1):
        if a[i] == 0:
            zeroes += 1
        else:
            inversions += zeroes
    return inversions

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    res = calc(a)

    for i in range(n):
        if a[i] == 0:
            a[i] = 1 - a[i]
            res = max(res, calc(a))
            a[i] = 1 - a[i]
            break 

    for i in range(n - 1, -1, -1):
        if a[i] == 1:
            a[i] = 1 - a[i]
            res = max(res, calc(a))
            a[i] = 1 - a[i]
            break 
    
    print(res)