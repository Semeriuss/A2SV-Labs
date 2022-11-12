for _ in range(int(input())):
    m = int(input())
    p = list(map(int, input().split()))

    count = 0
    j = 1
    i = 1
    INVALID = False
    while j < m:
        k = i
        print("---", i, j, p)
        while i < m:
            if p[i] < p[i - j]:
                if p[i - j] - p[i] != j:
                    print("ERROR",p, p[i - j], p[i], j, i)
                    INVALID = True 
                    break 
                print("%%%%%%%%%%%%%", p[i : i + j], p[i - j : i])
                p[i: i + j], p[i - j: i] = p[i - j: i], p[i: i + j]
                count += 1
            i += (j*2)
        if INVALID:
            break 
        i = k + (j*2)
        j *= 2
    
    if INVALID:
        print(-1)
    else:
        print(count, p)