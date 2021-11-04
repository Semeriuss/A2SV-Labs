import sys
from collections import defaultdict

sys.setrecursionlimit(90100)

input = sys.stdin.readline
n, target = tuple(list(map(int, input().split())))

input = sys.stdin.readline
portals = list(map(int, input().split()))

def pathExists(n, target, portals):
    transportaionMap = defaultdict(list)

    for i, cell in enumerate(portals):
        if ((i+1) + cell) <= n:
            transportaionMap[i + 1].append((i + 1) + cell)

    def dfs(graph, source, target):
        if source == target:
            return True

        for cell in graph[source]:
            if dfs(graph, cell, target):
                return True
        return False
    
    hasPath = dfs(transportaionMap, 1, target)
    return "YES" if hasPath else "NO"

print(pathExists(n, target, portals))


