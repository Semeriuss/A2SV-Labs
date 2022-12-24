from itertools import accumulate
n, q = map(int, input().split())
price = sorted(map(int, input().split()), reverse=True)
prefixsum = list(accumulate(price))
for _ in range(q):
    x, y = map(int, input().split())
    res = prefixsum[x - 1] - (prefixsum[x - y - 1] if x - y - 1 >= 0 else 0)
    print(res)
