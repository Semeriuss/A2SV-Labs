from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        output, visited = [], set()
        while left < right and top < bottom:
            for i in range(left, right):
                if (top, i) not in visited:
                    output.append(matrix[top][i])
                    visited.add((top, i))
            top += 1
            for j in range(top, bottom):
                if (j, right - 1) not in visited:
                    output.append(matrix[j][right - 1])
                    visited.add((j, right - 1))
            right -= 1
            for k in range(right - 1, left - 1, - 1):
                if (bottom - 1, k) not in visited:
                    output.append(matrix[bottom - 1][k])
                    visited.add((bottom - 1, k))
            bottom -= 1
            for l in range(bottom - 1, top - 1, - 1):
                if (l, left) not in visited:
                    output.append(matrix[l][left])
                    visited.add((l, left))
            left += 1
        return output

matrix = [[1,2,3], [4,5,6], [7,8,9]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
matrix = [[23,18,20,26,25],[24,22,3,4,4],[15,22,2,24,29],[18,15,23,28,28]]
print(Solution().spiralOrder(matrix))