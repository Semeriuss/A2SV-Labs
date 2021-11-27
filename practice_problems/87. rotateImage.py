from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        left, right = 0, len(matrix) - 1
        while left < right:
            top, bottom = left, right
            for level in range(right - left):

                topLeft = matrix[top][left + level]

                matrix[top][left + level] = matrix[bottom - level][left]
                matrix[bottom - level][left] = matrix[bottom][right - level]
                matrix[bottom][right - level] = matrix[top + level][right]
                matrix[top + level][right] = topLeft

            left += 1
            right -= 1
    
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(Solution().rotate(mat))


        
        