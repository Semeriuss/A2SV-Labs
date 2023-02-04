n, d = map(int, input().split())
s = input() 
steps = i = 0
while i < n:
    Found = False
    if i == n - 1:
        break
    for j in range(i + d, i, -1):
        if j < n and s[j] == '1':
            i = j
            Found = True
            break 
    steps += 1
    if not Found:
        steps = -1
        break
print(steps)

            