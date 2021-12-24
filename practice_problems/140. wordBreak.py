from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def dfs(index, dp):
            if index in dp: return dp[index]
            if index == len(s): return True
            for word in wordDict:
                if s[index:].startswith(word):
                    dp[index] = dfs(index + len(word))
                    if dp[index]: return True
            return False
        
        return dfs(0, {})