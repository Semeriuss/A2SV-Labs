n, m = map(int, input().split())
grid = []
cleared = []
for i in range(n):
    row = list(input())
    grid.append(row)
    cleared.append(row[:])

def crossRow(row):
    seen = set()
    toClear = set()
    for i in range(m):
        if grid[row][i] in seen:
            toClear.add(grid[row][i])
        else:
            seen.add(grid[row][i])
    
    for i in range(m):
        if grid[row][i] in toClear:
            cleared[row][i] = ""

def crossCol(col):
    seen = set()
    toClear = set()

    for j in range(n):
        if grid[j][col] in seen:
            toClear.add(grid[j][col])
        else:
            seen.add(grid[j][col])
    
    for j in range(n):
        if grid[j][col] in toClear:
            cleared[j][col] = ""


for i in range(n):
    crossRow(i)

for j in range(m):
    crossCol(j)

res = []
for i in range(n):
    res.append("".join(cleared[i]))

print("".join(res))