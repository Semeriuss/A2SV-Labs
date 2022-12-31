from collections import defaultdict, deque
n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

q = deque([0])
start = 0
vis = set()
while q:
    curr = q.popleft()
    if curr in vis: continue
    start = curr 
    vis.add(curr)
    for nbr in graph[curr]:
        if nbr not in vis:  
            q.append(nbr)

q = deque([(start, 0)])
vis = set()
res = 0
while q:
    curr, res = q.popleft()
    if curr in vis: continue
    vis.add(curr)
    for nbr in graph[curr]:
        if nbr not in vis:  
            q.append((nbr, res + 1))

print(res)


