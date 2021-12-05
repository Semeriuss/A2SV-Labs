from typing import List
class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        ROW = len(rowCosts)
        COL = len(colCosts)
        
        self.minimumCost = float("inf") 
        def fitsBoundary(row, col):
            return 0 <= row < ROW and 0 <= col < COL
        def dfs(src, dst, cost, visited):
            i, j = src
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_x, next_y = x + i, y + j
                if fitsBoundary(next_x, next_y) and (next_x, next_y) not in visited:
                    visited.add((next_x, next_y))
                    print("heree", cost, (next_x, next_y), dst, (next_x, next_y) == dst)
                    if not x:
                        cost += colCosts[next_y]
                    else:
                        cost += rowCosts[next_x]

                    if (next_x, next_y) == dst: 
                        print("ands")
                        self.minimumCost = min(cost, self.minimumCost)
                        return
                    dfs((next_x, next_y), dst, cost, visited)
                    visited.remove((next_x, next_y))
                    if not x:
                        cost -= colCosts[next_y]
                    else:
                        cost -= rowCosts[next_x]
        dfs(startPos, homePos, 0, set())
        return self.minimumCost

start = [1, 0]
end = [2, 3]
rowcost = [5, 4, 3]
colcost = [8, 2, 6, 7]

start = [1,2]
end = [3,3]
rowcost = [10,1,2,3]
colcost = [10,7,8,9]
print(Solution().minCost(tuple(start), tuple(end), rowcost, colcost))

