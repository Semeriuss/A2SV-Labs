for _ in range(int(input())):
    s = list(map(int, list(input())))
    n = len(s)
    missing = 3 
    found = [0, 0, 0]
    i, j = 0, 0
    res = float('inf')
    while j < n: 
        if not missing:
            if j - i < res:
                res = j - i 
            
            found[s[i] - 1] -= 1
            if not found[s[i] - 1]:
                missing += 1
            i += 1

        if missing:
            if not found[s[j] - 1]:
                missing -= 1
            found[s[j] - 1] += 1
            j += 1
    
    while i < j:
        if not missing:
            if j - i < res:
                res = j - i 
            
            found[s[i] - 1] -= 1
            if not found[s[i] - 1]:
                missing += 1
            i += 1
        else:
            break 

    print(res if res != float('inf') else 0)
        
            
