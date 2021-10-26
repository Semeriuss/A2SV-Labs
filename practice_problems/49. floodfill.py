from collections import deque
from typing import List, Tuple
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        colorToBeFilled = image[sr][sc]
        image[sr][sc] = newColor
        
        index = (sr, sc)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        
        def fitsBoundary(row, col):
            return 0 <= row < len(image) and 0 <= col < len(image[0])
        
        def bfs(index: 'Tuple', image: List[List[int]]):
            
            visited = set()
            queue = deque([index])
            visited.add(index)
            
            while queue:
                current_row, current_col = queue.popleft()
                for direction in directions:
                    next_row, next_col = 0, 0
                    
                    next_row = current_row + direction[0]
                    next_col = current_col + direction[1]
                    
                    next_state = next_row, next_col
                    
                    if fitsBoundary(next_row, next_col) and next_state not in visited:
                        if image[next_row][next_col] == colorToBeFilled:
                            image[next_row][next_col] = newColor
                            queue.append(next_state)
                            visited.add(next_state)
        
        bfs(index, image)
        return image
            
            