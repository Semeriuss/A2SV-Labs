from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        def fitsBoundary(x, y):
            return 0 <= x < ROW and 0 <= y < COL          

        minTime = 0
        path = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        queue = deque()
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 2:
                    queue.append((row, col))
                
        visited = set()
        while queue:
            curr_x, curr_y = queue.popleft()
            foundFresh = False
            for x, y in path:
                next_x, next_y = curr_x + x, curr_y + y
                if fitsBoundary(next_x, next_y) and (next_x, next_y) not in visited and grid[next_x][next_y] == 1:
                    queue.append((next_x, next_y))
                    visited.add((next_x, next_y))
                    foundFresh = True

            if foundFresh:
                minTime += 1
        
        for row in range(ROW):
            for col in range(COL):
                if (row, col) not in visited and grid[row][col] == 1:
                    return -1

        return minTime
                 
            