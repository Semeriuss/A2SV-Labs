from typing import List
from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        edgeCount = [0]*n

        if n <= 2: return [node for node in range(n)]
        for i, edge in enumerate(edges):
            graph[i]
            a, b = edge
            graph[a].append(b)
            edgeCount[a] += 1
            graph[b].append(a)
            edgeCount[b] += 1

        que = deque([node for node in graph if edgeCount[node] == 1])
        totalNodes = n
        # print(edgeCount, graph)
        # print(que)
        while totalNodes > 2:
            # print(que, graph)
            totalNodes -= len(que)

            for _ in range(len(que)):
                curr = que.popleft()
                for neighbor in graph[curr]:
                    print(edgeCount, que)
                    edgeCount[neighbor] -= 1
                    # print(edgeCount, que)
                    print(curr, neighbor, edgeCount)
                    if edgeCount[neighbor] ==  1:
                        que.append(neighbor)

        print(que)
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
