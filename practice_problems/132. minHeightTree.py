from typing import List
from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for i, edge in enumerate(edges):
            graph[i]
            a, b = edge
            graph[a].append(b)
            graph[b].append(a)

        depthList = [n]*n
        minDepth = n
        for i in range(n):
            depthList[i] = self.maxDepth(graph, i, set(), 0)
            minDepth = min(minDepth, depthList[i])
        
        return [node for node, depth in enumerate(depthList) if depth == minDepth]
    
    def maxDepth(self, graph: dict, node: int, visited: set, depth: int) -> int:
        if node in visited:
            return 0
        visited.add(node)
        count = depth
        for neighbor in graph[node]:
            count = max(count, self.maxDepth(graph, neighbor, visited, depth + 1))
        return count

n = 4
edges = [[1,0],[1,2],[1,3]]

n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]

print(Solution().findMinHeightTrees(n, edges))
