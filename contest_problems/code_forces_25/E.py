n, k = map(int, input().split())
a = [1]*k
n -= k
i = 0
while n > 0 and i < k:
    while a[i] <= n:
        n -= a[i]
        a[i] *= 2
    i += 1
if n:
    print("NO")
else:
    print("YES")
    print(*a)
