from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        self.perimeter = 0

        ROW = len(grid)
        COL = len(grid[0])

        path = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def fitsBoundary(i, j):
            return 0 <= i < ROW and 0 <= j < COL

        def findConnectedIslands(row, col):
            for x, y in path:
                new_x, new_y = row + x, col + y
                if fitsBoundary(new_x, new_y) and grid[new_x][new_y]:
                    self.perimeter -= 1

        for row in range(ROW):
            for col in range(COL):
                if grid[row][col]:
                    self.perimeter += 4
                    findConnectedIslands(row, col)
        
        return self.perimeter
            

