from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROW = len(board)
        COL = len(board[0])

        path = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def fitsBoundary(x, y):
            return 0 <= x < ROW and 0 <= y < COL

        def connectToBorder(i, j):
            for x, y in path:
                next_x, next_y = i + x, j + y
                if fitsBoundary(next_x, next_y) and board[next_x][next_y] == 'O':
                    board[next_x][next_y] = 'B'
                    connectToBorder(next_x, next_y)
        
        for row in range(ROW):
            if board[row][0] == 'O':
                board[row][0] = 'B'
                connectToBorder(row, 0)
            if board[row][COL - 1] == 'O':
                board[row][COL - 1] = 'B'
                connectToBorder(row, COL - 1)
        
        for col in range(COL):
            if board[0][col] == 'O':
                board[0][col] = 'B'
                connectToBorder(0, col)
            if board[ROW - 1][col] == 'O':
                board[ROW - 1][col] = 'B'
                connectToBorder(ROW - 1, col)
            
        for row in range(ROW):
            for col in range(COL):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
        
        for row in range(ROW):
            for col in range(COL):
                if board[row][col] == 'B':
                    board[row][col] = 'O'
     
        return board

board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']
        ]
board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']
        ]
print(Solution().solve(board))
                
               

