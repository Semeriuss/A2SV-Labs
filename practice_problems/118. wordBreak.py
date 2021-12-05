from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.exists = False
        ROW = len(board)
        COL = len(board[0])

        def fitsBoundary(x, y):
            return 0 <= x < ROW and 0 <= y < COL

        def wordExists(src, index, path, visited):
            if index >= len(word) + 1 or "".join(path) == word: return True
            x, y = src
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_x, next_y = x + i, y + j
                # yes = "hi" if not fitsBoundary(next_x, next_y) else board[next_x][next_y]
                print("nexts", path, " ", index)
                if fitsBoundary(next_x, next_y) and word[index] == board[next_x][next_y] and (next_x, next_y) not in visited:
                    print("here", word[index], (next_x, next_y), " ", board[next_x][next_y], index + 1 == len(word))
                    path.append(board[next_x][next_y])
                    visited.add((next_x, next_y))
                    print("joined   ", "".join(path), "".join(path) == word)
                    if "".join(path) == word: 
                        self.exists = True
                        return self.exists
                    wordExists((next_x, next_y), 1 + index, path, visited)
                    path.pop()
                    visited.remove((next_x, next_y))
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