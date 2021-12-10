from functools import lru_cache
class Solution:
    @lru_cache(maxsize = None)
    def numDecodings(self, s: str) -> int:
        if s and s[0] == '0': return 0
        dp = [0 for _ in range(len(s) + 1)]
        dp[0 : 2] = [1, 1]
        for i in range(2, len(s) + 1):
            if 0 < int(s[i - 1: i]) <= 9:
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 2: i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]
s = "12"
print(Solution().numDecodings(s))