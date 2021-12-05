from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW = len(board)
        COL = len(board[0])

        def fitsBoundary(x, y):
            return 0 <= x < ROW and 0 <= y < COL

        def wordExists(src, index, visited):
            if index >= len(word) - 1: return True
            x, y = src
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_x, next_y = x + i, y + j
                yes = "hi" if not fitsBoundary(next_x, next_y) else board[next_x][next_y]
                print("nexts", yes, " ", index)
                if fitsBoundary(next_x, next_y) and (next_x, next_y) not in visited and word[index] == board[next_x][next_y]:
                    visited.add((next_x, next_y))
                    if index + 1 == len(word): return True
                    print("here", word[index], (next_x, next_y), " ", index, index + 1 == len(word))
                    wordExists((next_x, next_y), 1 + index, visited)
                    visited.remove((next_x, next_y))
            return False

        
        start = word[0]
        for row in range(ROW):
            for col in range(COL):
                if board[row][col] == start and wordExists((row, col), 1, set()):
                    return True
        return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(Solution().exist(board, word))