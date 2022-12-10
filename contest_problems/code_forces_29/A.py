for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    res = (1, 1)
    f = - 1

    i, j = 0, 0
    seen = {a[i] : 1}
    distinct = 1
    while i <= j and j < n:
        cur_f = j - i - distinct 
        if cur_f > f:
            res = i + 1, j + 1
            f = cur_f
            seen[a[i]] -= 1
            if seen[a[i]] == 0:
                distinct -= 1
        j += 1
        if j < n and a[j] not in seen:
            seen[a[j]] = seen.get(a[j], 0) + 1
            if seen[a[j]] == 1:
                distinct += 1
        
    print(*res)
