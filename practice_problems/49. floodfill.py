from typing import Collection, List
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        colorToBeRemoved = image[sr][sc]
        image[sr][sc] = newColor

        def bfs(sr, sc, image, colorToBeRemoved, newColor, rowLength, colLength, visited):
            dirs = [(0,1), (0, -1), (1, 0), (-1, 0)]
            queue = deque([(sr, sc)])
            visited = set()

            while queue:
                sr, sc = queue.popleft()
                for dir in dirs:
                    current_row, current_col = 0, 0
                    current_row = sr + dir[0]
                    current_col = sc + dir[1]
                    if 0 <= current_row < rowLength and 0 <= current_col < colLength:
                        if image[current_row][current_col] == colorToBeRemoved and (current_row, current_col) not in visited:
                            image[current_row][current_col] = newColor
                            queue.append((current_row, current_col))
                            visited.add((current_row, current_col))
        bfs(sr, sc, image, colorToBeRemoved, newColor, len(image), len(image[0]), set())

            

        def dfs(sr, sc, image, colorToBeRemoved, newColor, rowLength, colLength, visited):
            dirs = [(0,1), (0, -1), (1, 0), (-1, 0)]
            for dir in dirs:
                current_row, current_col = 0, 0
                current_row = sr + dir[0]
                current_col = sc + dir[1]
                if 0 <= current_row < rowLength and 0 <= current_col < colLength:
                    if image[current_row][current_col] == colorToBeRemoved and (current_row, current_col) not in visited:
                        image[current_row][current_col] = newColor
                        visited.add((current_row, current_col))
                        dfs(current_row, current_col, image, colorToBeRemoved, newColor, rowLength, colLength, visited)
        # dfs(sr, sc, image, colorToBeRemoved, newColor, len(image), len(image[0]), set())
        return image
                    


print(Solution().floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
                


