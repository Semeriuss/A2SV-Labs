n, m = list(map(int, input().split()))
parent = list(range(n))
size = [1] * n 

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    a, b = sorted([find(x), find(y)], key=lambda x : size[x])
    if a != b:
        parent[a] = b 
        size[b] += size[a]

for _ in range(m):
    k = list(map(int, input().split()))
    for i in range(1, len(k) - 1):
        union(k[i] - 1, k[i + 1] - 1)

res = []
for i in range(n):
    res.append(size[find(i)])

print(*res)