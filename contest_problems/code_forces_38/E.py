from collections import Counter
for _ in range(int(input())):
    n = int(input())
    freq = Counter(map(int, input().split()))
    freqGrp = Counter(freq.values())

    res = n
    for x in freqGrp:
        temp = 0
        for y in freqGrp:
            if x > y:
                temp += y * freqGrp[y]
            else:
                temp += (y - x) * freqGrp[y]
        res = min(res, temp)
    print(res)
