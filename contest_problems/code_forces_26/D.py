from collections import defaultdict
n, m = map(int, input().split())
parent = list(range(n + 1))
children = [1]*(n + 1)

def find(node):
    if node != parent[node]:
        parent[node] = parent[parent[node]]
    return parent[node]

def union(u, v):
    root1, root2 = sorted([find(u), find(v)], key=lambda x : children[x])
    if root1 != root2:
        parent[root1] = root2
        children[root2] += children[root1]

graph = defaultdict(int)
invalids = set()
for _ in range(m):
    u, v = map(int, input().split())
    union(u, v)
    graph[u] += 1
    graph[v] += 1
    if graph[u] > 2:
        invalids.add(u)
        invalids.add(v)
    if graph[v] > 2:
        invalids.add(v)
        invalids.add(u)
    
for node, edgeCount in graph.items():
    root = find(node)
    if edgeCount == 1 or root in invalids:
        invalids.add(node)
        invalids.add(root)


for node in range(1, n + 1):
    root = find(node)
    if node in invalids:
        invalids.add(root)
    

found = set()
res = 0
for node, edgeCount in graph.items():
    root = find(node)
    if edgeCount == 2 and root not in invalids and root not in found:
        found.add(root)
        res += 1

print(res)





