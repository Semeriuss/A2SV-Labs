from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.exists = False
        ROW = len(board)
        COL = len(board[0])
        word = list(word)
        def fitsBoundary(x, y):
            return 0 <= x < ROW and 0 <= y < COL

        def wordExists(src, index, path, visited):
            if index >= len(word) + 1: return True
            x, y = src
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_x, next_y = x + i, y + j
                if fitsBoundary(next_x, next_y) and word[index] == board[next_x][next_y] and (next_x, next_y) not in visited:
                    visited.add((next_x, next_y))
                    if index + 1 == len(word): 
                        self.exists = True
                        return self.exists
                    path.append(board[next_x][next_y])
                    wordExists((next_x, next_y), 1 + index, path, visited)
                    visited.remove((next_x, next_y))
                    path.pop()
            return self.exists

        
        start = word[0]
        for row in range(ROW):
            for col in range(COL):
                if board[row][col] == start and wordExists((row, col), 1, [start], set()):
                    return True
        return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"

board = [
    ["A","B","C","E"],
    ["S","F","E","S"],
    ["A","D","E","E"]
    ]
word = "ABCESEEEFS"
print(Solution().exist(board, word))