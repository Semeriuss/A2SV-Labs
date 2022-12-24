for _ in range(int(input())):
    n, m = map(int, input().split())
    x = y = res = 0
    idx = 1
    while y < m:
        res += idx 
        y += 1
        if y < m: idx += 1
    
    idx += m
    x += 1
    while x < n:
        res += idx
        x += 1
        idx += m
    
    print(res)