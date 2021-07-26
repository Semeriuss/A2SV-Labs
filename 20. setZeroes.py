def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        rowHasZero = False
        colHasZero = False
        
        def nullifyRow(matrix, row):
            for i in range(len(matrix[row])):
                matrix[row][i] = 0

        def nullifyCol(matrix, col):
            for i in range(len(matrix)):
                for i in range(len(matrix)):
                    matrix[i][col] = 0

        for i in range(len(mat[0])):
            if mat[0][i] == 0:
                rowHasZero = True
                break

        for i in range(len(mat)):
            if mat[i][0] == 0:
                colHasZero = True
                break

        for i in range(1, len(mat)):
            for j in range(1, len(mat[0])):
                if mat[i][j] == 0:
                    mat[i][0] = 0
                    mat[0][j] = 0

        for i in range(1, len(mat[0])):
            if mat[0][i] == 0:
                nullifyCol(mat, i)

        for j in range(1, len(mat)):
            if mat[j][0] == 0:
                nullifyRow(mat, j)

        if rowHasZero:
            nullifyRow(mat, 0)

        if colHasZero:
            nullifyCol(mat, 0)
                
