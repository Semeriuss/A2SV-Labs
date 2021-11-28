from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROW = len(matrix)
        COL = len(matrix[0])

        path = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def dfs(mat, src, visited, res):
            a, b = src
            if src in visited or a >= ROW or b >= COL or a < 0 or b < 0:
                return 
            visited.add(src)
            for x, y in path:
                next_a, next_b = a + x, b + y
                if mat[a][b] not in visited:
                    visited.add(mat[a][b])
                    res.append(mat[a][b])
                if (next_a, next_b) not in visited:
                    dfs(mat, (next_a, next_b), visited, res)
        ans = []
        dfs(matrix, (0, 0), set(), ans)
        return ans


matrix = [[1,2,3], [4,5,6], [7,8,9]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(Solution().spiralOrder(matrix))






# def dfs(mat, i, j, visited):
    # if (i >= ROW and j >= COL) or (i < 0 ):
    #     return 
    
    # if j < COL:
    #     if (i, j) not in visited:
    #         visited.add((i, j))
    #         print(mat[i, j])
    #     dfs(mat, i, j + 1)

    # if i < ROW:
    #     if (i, j) not in visited:
    #         visited.add((i, j))
    #         print(mat[i, j])
    #     dfs(mat, i + 1, j)
    
    # if j == COL - 1:
    #     if (i, j) not in visited:
    #         visited.add((i, j))
    #         print(mat[i, j])
    #     dfs(mat, i, j - 1)

    # if i == COL - 1:
    #     if (i, j) not in visited:
    #         visited.add((i, j))
    #         print(mat[i, j])
    #     dfs(mat, i - 1, j)
    




