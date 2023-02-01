from ast import List


class Solution:
    # O(N*M) time and O(N*M) space
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        N, M = len(mat), len(mat[0])
        answer = [[0] * M for _ in range(N)]

        dp = mat[:][:]
        for i in range(N):
            for j in range(M):
                dp[i][j] += (dp[i - 1][j] if (i - 1) >= 0 else 0) + \
                            (dp[i][j - 1] if (j - 1) >= 0 else 0) - \
                            (dp[i - 1][j - 1] if (i - 1)
                             >= 0 and (j - 1) >= 0 else 0)

        for i in range(N):
            ri = max(0, i - k)
            rf = min(N - 1, i + k)
            for j in range(M):
                ci = max(0, j - k)
                cf = min(M - 1, j + k)
                answer[i][j] = dp[rf][cf]
                if ri > 0:
                    answer[i][j] -= dp[ri - 1][cf]
                if ci > 0:
                    answer[i][j] -= dp[rf][ci - 1]
                if ri > 0 and ci > 0:
                    answer[i][j] += dp[ri - 1][ci - 1]

        return answer
