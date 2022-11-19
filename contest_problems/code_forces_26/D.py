n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
invalids = set()
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
valids = set()
for i in range(n + 1):
    if len(graph[i]) == 2:
        valids.add(i)

res = 0
while valids:
    node = valids.pop()
    left, right = graph[node]
    while right in valids:
        valids.remove(right)
        next_left, next_right = graph[right]
        if next_left in valids:
            right = next_left
        elif next_right in valids:
            right = next_right 
        else:
            break 
        if left == right:
            res += 1
            
print(res)





