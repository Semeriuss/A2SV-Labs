n = int(input())
a = list(map(int, input().split()))

res = cursum = 1

for i in range(1, n):
    if a[i] >= a[i - 1]:
        cursum += 1
    else:
        res = max(cursum, res)
        cursum = 1
    res = max(cursum, res)

print(res)
