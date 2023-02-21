from collections import defaultdict, deque
from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        seen = set()
        for u, v in edges:
            graph[u].append(v)
            seen.add(v)

        res = set()
        que = deque(sorted([i for i in range(n) if len(
            graph[i]) > 0], key=lambda x: -len(graph[x])))
        while que:
            curr = que.popleft()
            if curr not in seen:
                res.add(curr)
                seen.add(curr)
                for neigh in graph[curr]:
                    if neigh not in seen:
                        seen.add(neigh)
                    if neigh in res:
                        res.remove(neigh)
        return res
