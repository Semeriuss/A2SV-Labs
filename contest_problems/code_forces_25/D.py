for _ in range(int(input())):
    m = int(input())
    p = list(map(int, input().split()))
    p = [0] + p
    count = 0
    j = 1
    INVALID = False
    while j <= m:
        k = j//2
        i = 1
        while i <= m:
            diff = p[i] - p[i + k]
            if abs(diff) != k:
                INVALID = True 
                break 
            if diff > 0:
                p[i], p[i + k] = p[i + k], p[i]
                count += 1
            i += j
        if INVALID:
            break 
        j *= 2
    
    if INVALID:
        print(-1)
    else:
        print(count)