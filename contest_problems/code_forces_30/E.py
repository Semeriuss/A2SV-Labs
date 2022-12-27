s = input()
t = input()
n = len(s)
m = len(t)
 
 
dp = [[0] * (n + 1) for _ in range(m + 1)]
 
for i in range(n):
    dp[m][i] = n - i
 
for j in range(m):
    dp[j][n] = m - j
 
for i in range(m - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        if s[j] == t[i]:
            dp[i][j] = dp[i + 1][j + 1]
        else:
            insert = dp[i][j + 1]
            replace = dp[i + 1][j + 1]
            delete = dp[i + 1][j]
            dp[i][j] = 1 + min(insert, replace, delete)
 

 
print(dp[0][0])
i = 0
j = 0
while i < m and j < n:
    if t[i] == s[j]:
        i += 1
        j += 1
    else:    
        insert = dp[i + 1][j] if i <= m else float('inf')
        replace = dp[i + 1][j + 1] if i <= m and j <= n else float('inf')
        delete = dp[i][j + 1] if j <= n else float('inf')
 
        if insert <= replace and insert <= delete:
            print('INSERT', i + 1, t[i])
            i += 1
        
        elif replace <= insert and replace <= delete:
            print('REPLACE', i + 1, t[i])
            i += 1
            j += 1
 
        else:
            print('DELETE', i + 1)
            j += 1

while j < n:
    print('DELETE', i + 1)
    j += 1

while i < m:
    print('INSERT', i + 1, t[i])
    i += 1
