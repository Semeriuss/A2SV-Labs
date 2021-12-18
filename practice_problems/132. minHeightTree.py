from typing import List
from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)

        if n <= 2: return [node for node in range(n)]
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        que = deque([node for node in graph if len(graph[node]) == 1])
        totalNodes = n
        while totalNodes > 2:
            totalNodes -= len(que)

            for _ in range(len(que)):
                curr = que.popleft()
                for neighbor in graph[curr]:
                    graph[neighbor].remove(curr)
                    if len(graph[neighbor]) ==  1:
                        que.append(neighbor)

        return que

n = 4
edges = [[1,0],[1,2],[1,3]]

# n = 6
# edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]

n = 6
edges = [[0,1],[0,2],[0,3],[3,4],[4,5]]

# n = 5
# edges = [[0,1],[0,2],[2,3],[3,4]]
print(Solution().findMinHeightTrees(n, edges))
