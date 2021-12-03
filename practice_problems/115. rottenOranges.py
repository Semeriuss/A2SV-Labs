from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        def fitsBoundary(x, y):
            return 0 <= x < ROW and 0 <= y < COL          
        
        minTime, oneCount = 0, 0
        queue = deque()
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 2: queue.append((row, col))
                if grid[row][col] == 1: oneCount += 1 

        while queue:
            for _ in range(len(queue)):
                curr_x, curr_y = queue.popleft()
                for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    next_x, next_y = curr_x + x, curr_y + y
                    if fitsBoundary(next_x, next_y) and grid[next_x][next_y] == 1:
                        grid[next_x][next_y] = 2
                        oneCount -= 1
                        queue.append((next_x, next_y))    
            minTime += 1
        
        return max(0, minTime - 1) if not oneCount else -1
# [[2,1,1],[1,1,0],[0,1,1]]
# [[2,1,1],[0,1,1],[1,0,1]]
# [[0,2]]
# [[0]]
# [[1]]
# [[2]]
# [[1,1,1]]
# [[2,0,1]]
# [[2,0,1], [1,0,0],[0,0,0]]
# [[2,1,1,2,1,1,0,1,1,0],[0,1,2,1,1,0,1,1,1,2],[2,1,1,0,1,2,1,0,1,0],[0,1,2,1,1,0,1,1,1,2],[2,1,1,0,1,2,1,0,1,0],[2,1,1,2,1,1,0,1,1,0]]
# [[2,0,1],[0,1,1],[1,1,1]]
# [[1,1,1],[1,1,2]]
# [[1,1,1,1,1],[0,0,0,0,0]]
# [[1,0,0],[0,0,0],[2,2,2]]