from typing import List


class Solution:
    # O(N*N) time and O(N) space
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        mapping = sorted([(age, score) for score, age in zip(scores, ages)])
        dp = [mapping[i][1] for i in range(n)]

        for i in range(n - 1, -1, -1):
            mAge, mScore = mapping[i]
            for j in range(i + 1, n):
                age, score = mapping[j]
                if mScore <= score:
                    dp[i] = max(dp[i], mScore + dp[j])

        return max(dp)
