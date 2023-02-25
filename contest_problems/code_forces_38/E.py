from collections import Counter
from heapq import heappush, heappop
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    freq = Counter(a)
    k = max(freq.values())
    rep = [0] * (k + 1)
    for num in freq:
        rep[freq[num]] += 1
    heap = []
    for i in range(1, k + 1):
        if (rep[i] * i) != 0:
            heappush(heap, (-(rep[i] * i), -i, -rep[i]))

    _, count, res = heappop(heap)
    res, count = -res, -count
    ans = 0
    ret = [float('-inf')] * (k + 1)
    while heap:
        _, freq, cur = heappop(heap)
        cur, freq = -cur, -freq
        if freq > count:
            ans += (cur * (freq - count))
        else:
            ans += (cur * freq)

    print(ans)
