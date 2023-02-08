from collections import defaultdict
from typing import List


class Solution:
    # O(N) time and space
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        count = defaultdict(int)

        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)
            count[a] += 1
            count[b] += 1

        def dfs(cur):
            if cur in visited:
                return
            visited.add(cur)
            res.append(cur)
            for nbr in graph[cur]:
                if nbr not in visited:
                    count[nbr] -= 1
                    dfs(nbr)

        visited = set()
        res = []
        for num in count:
            if count[num] < 2:
                dfs(num)
        return res
