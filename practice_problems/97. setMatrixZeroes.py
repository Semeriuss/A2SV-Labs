from typing import List


class Solution:
    def setColumnZeroes(self, matrix: List[List[int]], column: int) -> None:
        for row in range(len(matrix)):
            matrix[row][column] = 0
    
    def setRowZeroes(self, matrix: List[List[int]], row: int) -> None:
        for column in range(len(matrix[0])):
            matrix[row][column] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        colHasZero, rowHasZero = False, False
        for col in range(len(matrix[0])):
            if matrix[0][col] == 0:
                rowHasZero = True
                break
        
        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                colHasZero = True
                break             
        print(rowHasZero)
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0

        for col in range(1, len(matrix[0])):
            if matrix[0][col] == 0:
                self.setColumnZeroes(matrix, col)
    
        for row in range(1, len(matrix)):
            if matrix[row][0] == 0:
                self.setRowZeroes(matrix, row) 
        
        if colHasZero: self.setColumnZeroes(matrix, 0)
        print(matrix, rowHasZero)
        if rowHasZero: self.setRowZeroes(matrix, 0)      
        return matrix
            

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
matrix = [[1,0,3]]
print(Solution().setZeroes(matrix))