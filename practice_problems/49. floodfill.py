from collections import deque
from typing import List, Tuple
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        colorToBeFilled = image[sr][sc]
        image[sr][sc] = newColor
        path = [(0, 1), (0, -1), (1, 0), (-1, 0)]        
        
        def fitsBoundary(row, col):
            return 0 <= row < len(image) and 0 <= col < len(image[0])
        
        def dfs(sr, sc):
            if not fitsBoundary(sr, sr): return 
            for x, y in path:
                next_x, next_y = sr + x, sc + y 
                if fitsBoundary(next_x, next_y) and image[next_x][next_y] == colorToBeFilled:
                    image[next_x][next_y] = newColor
                    dfs(next_x, next_y)
        
        dfs(sr, sc)
        return image
            
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2  
print(Solution().floodFill(image, sr, sc, newColor))