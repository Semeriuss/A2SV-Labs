from collections import Counter
s = input()
n = len(s)
res = ""
Found = False
for c, f in Counter(s).items():
    if f >= 100:
        res = c*100
        Found = True 
        break 

if Found:
    print(res)
else:
    if n > (26*99 + 1):
        s = s[:(26*99 + 1)]
    t = s[::-1]
    n = len(t)
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1): 
            if s[i - 1] == t[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1] 
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    res = []
    i = j = n
    while i > 0 and j > 0:
        if s[i - 1] == t[j - 1]:
            res.append(s[i - 1])
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
    
    if len(res) > 100:
        print("".join(res[:50] + res[:50][::-1]))
    else:
        print("".join(res))