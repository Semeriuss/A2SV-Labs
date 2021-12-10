from functools import lru_cache
class Solution:
    @lru_cache(maxsize = None)
    def numDecodings(self, s: str) -> int:
        if s and s[0] == '0': return 0
        if len(s) == 1 or s == "": return 1

        if len(s) >= 2:
            if s[0 : 2] <= '26':
                return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
            return self.numDecodings(s[1:])

s = "12"
print(Solution().numDecodings(s))