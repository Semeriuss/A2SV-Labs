def twoButtons(n, m, memo):
    if m <= 0:
        return 
    
    if n == m:
        return 0
    
    else:
        
        if m % 2 != 0:
            memo[m] = twoButtons(n, m + 1, memo)
            return 1 + memo[m]
        else:
            memo[m] = twoButtons(n, m//2, memo)
            return 1 + memo[m]

if __name__ == "__main__":
    n, m = map(int, input().split())
    if m > n:
        print(twoButtons(n, m, {}))
    else:
        print(n - m)