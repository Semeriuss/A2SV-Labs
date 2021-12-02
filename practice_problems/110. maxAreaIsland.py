from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        self.maxOnes = 0

        ROW = len(grid)
        COL = len(grid[0])

        path = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def fitsBoundary(i, j):
            return 0 <= i < ROW and 0 <= j < COL

        def countOnes(row, col, visited):
            visited.add((row, col))
            count = 1
            for x, y in path:
                new_x, new_y = row + x, col + y
                if fitsBoundary(new_x, new_y) and (new_x, new_y) not in visited and grid[new_x][new_y]:
                    count += countOnes(new_x, new_y, visited)
            return count

        visited = set()
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col]:
                    self.maxOnes = max(self.maxOnes, countOnes(row, col, visited))
        return self.maxOnes