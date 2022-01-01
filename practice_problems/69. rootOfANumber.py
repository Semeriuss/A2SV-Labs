def root(x, n):
    if x == 0:
        return 0

    lower = 0
    upper = x
    mid = (lower + upper)/2

    while (mid - lower >= 0.001):
        if pow(mid, n) > x:
            upper = mid
        elif pow(mid, n) < x:
            lower = mid
        else:
            break
        mid = (lower + upper)/2
        
        
    
    print(upper, lower, mid)
    return (lower + upper)/2

x = 7
n = 3
print(root(x, n))