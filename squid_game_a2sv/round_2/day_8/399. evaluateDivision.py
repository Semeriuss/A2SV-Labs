import collections
from typing import List


class Solution:
    # O(N * (q + e)) time and O(e) space
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        mapper = collections.defaultdict(dict)
        for i, equation in enumerate(equations):
            x, y = equation
            mapper[x][y] = values[i]
            mapper[y][x] = 1/values[i]
            mapper[x][x] = 1.0
            mapper[y][y] = 1.0

        visited = set()

        def findPath(src, dst, currvalue):
            if src == dst:
                return currvalue * mapper[src][dst]
            visited.add(src)
            for k in mapper[src]:
                if k not in visited:
                    res = findPath(k, dst, currvalue * mapper[src][k])
                    if res != -1:
                        return res
            return -1

        res = [-1.0]*len(queries)
        FOUND_MATCH = False
        for i, (a, b) in enumerate(queries):
            if a not in mapper or b not in mapper:
                res[i] = -1.0
            elif a == b:
                res[i] = 1.0
            elif b in mapper[a]:
                res[i] = mapper[a][b]
            else:
                for u in mapper[a]:
                    print(u, a, "here")
                    if u == a:
                        continue
                    ret = findPath(u, b, mapper[a][u])
                    if ret:
                        res[i] = ret
                        break
                else:
                    res[i] = -1.0
                visited.clear()
        return res
