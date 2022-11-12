from bisect import bisect_right
for _ in range(int(input())):
    n, c = input().split()
    s = input()
    n = int(n)
    res = 0
    if c != 'g':
        cPos = [i for i, char in enumerate(s) if char == c]
        gPos = [i for i, char in enumerate(s) if char == 'g']
        gPos.append(gPos[0] + n)
        currMin = 0
        for pos in gPos:
            i = bisect_right(cPos, pos)
            if i == 0 or currMin >= len(cPos):
                continue 
            else:
                res = max(res, pos - cPos[currMin])
                currMin = i        
    print(res)
