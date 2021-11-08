t = int(input())

tests = []
for i in range(t):
    n = int(input())
    mat = []
    for i in range(2):
        mat.append(list(map(int, input().split())))
    tests.append((n, mat))
    
def coinRows(n, mat):

    suffix = [0]
    for num in mat[0][::-1]:
        suffix.append(suffix[-1] + num)
    
    prefix = [0]
    for num in mat[1]:
        prefix.append(prefix[-1] + num)
    
    minScore = float("inf")
    for i in range(n):
        score1 = suffix[n - i - 1] 
        score2 = prefix[i]

        minScore = min(minScore, max(score1, score2))
    
    return minScore

res = []
for test in tests:
    n, mat = test
    res.append(coinRows(n, mat))

print(*res, sep="\n")
