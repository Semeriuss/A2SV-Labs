from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.islands = 0

        ROW = len(grid)
        COL = len(grid[0])

        path = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def fitsBoundary(row, col):
            return 0 <= row < ROW and 0 <= col < COL

        def visitIsland(row, col, visited):
            visited.add((row, col))
            for x, y in path:
                new_x, new_y = row + x, col + y
                if fitsBoundary(new_x, new_y) and int(grid[new_x][new_y]) and (new_x, new_y) not in visited:
                    visitIsland(new_x, new_y, visited)

        visited = set()
        for row in range(ROW):
            for col in range(COL):
                if int(grid[row][col]) and (row, col) not in visited:
                    self.islands += 1
                    visitIsland(row, col, visited)
        
        return self.islands
