import collections
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        visited = set()
        ROWS, COLS = len(board), len(board[0])
        def dfs(pos, wordIndex):

            if wordIndex == len(word):
                return True
            
            x, y = pos
            if x < 0 or x >= ROWS or y < 0 or y >= COLS or pos in visited or board[x][y] != word[wordIndex]:
                return False

            visited.add(pos)
            res = (dfs((x + 1, y), wordIndex + 1) or
                    dfs((x - 1, y), wordIndex + 1) or
                    dfs((x, y + 1), wordIndex + 1) or 
                    dfs((x, y - 1), wordIndex + 1))
            visited.remove(pos)
            return res
        for row in range(ROWS):
            for col in range(COLS):
                if dfs((row, col), 0):
                    return True
        return False

print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
            


            



