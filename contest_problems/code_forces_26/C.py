from itertools import accumulate
for _ in range(int(input())):
    n = int(input())
    red = list(map(int, input().split()))
    m = int(input())
    blue = list(map(int, input().split()))

    suffix_red = list(accumulate(reversed(red)))[::-1]
    suffix_blue = list(accumulate(reversed(blue)))[::-1]

    res = 0
    i, j = 0, 0
    total = 0
    while i < n and j < m:
        if red[i] >= blue[j]:
            if red[i] >= 0 or suffix_red[i] >= suffix_blue[j]:
                total += red[i]
                i += 1
            else:
                total += blue[j]
                j += 1
        else:
            if blue[j] >= 0 or suffix_blue[j] >= suffix_red[i]:
                total += blue[j]
                j += 1
            else:
                total += red[i]
                i += 1
        res = max(res, total)
    
    while i < n:
        total += red[i]
        res = max(res, total)
        i += 1
    
    while j < m:
        total += blue[j]
        res = max(res, total)
        j += 1
    
    print(res)