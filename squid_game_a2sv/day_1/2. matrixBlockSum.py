from ast import List


class Solution:
    # O(N*M * N^2) time, O(N^2) auxiliary space
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        N, M = len(mat), len(mat[0])
        answer = [[0] * M for _ in range(N)]

        def getSum(row_range, col_range):
            ri, rf = row_range
            ci, cf = col_range
            total = 0
            for r in range(ri, rf + 1):
                for c in range(ci, cf + 1):
                    total += mat[r][c]
            return total

        for i in range(N):
            ri = max(0, i - k)
            rf = min(N - 1, i + k)
            for j in range(M):
                ci = max(0, j - k)
                cf = min(M - 1, j + k)
                answer[i][j] += getSum((ri, rf), (ci, cf))

        return answer
