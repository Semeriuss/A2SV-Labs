from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        N = len(word)
        self.exists = False
        ROW = len(board)
        COL = len(board[0])
        
        if N > ROW * COL: return False
        def fitsBoundary(x, y):
            return 0 <= x < ROW and 0 <= y < COL

        def wordExists(x, y, index):
            if self.exists: return 

            if index == len(word): 
                self.exists = True
                return 

            if not fitsBoundary(x, y): return
            if word[index] != board[x][y]: return 

            tmp = board[x][y]
            board[x][y] = "#"
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_x, next_y = x + i, y + j
                wordExists(next_x, next_y, 1 + index)
            board[x][y] = tmp
        
        start = word[0]
        for row in range(ROW):
            for col in range(COL):
                if self.exists: return True
                if board[row][col] == start:
                    wordExists(row, col, 0)
        return self.exists

board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]]
word = "ABCCED"

# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCB"

# board = [
#     ["A","B","C","E"],
#     ["S","F","E","S"],
#     ["A","D","E","E"]
#     ]
# word = "ABCESEEEFS"
print(Solution().exist(board, word))