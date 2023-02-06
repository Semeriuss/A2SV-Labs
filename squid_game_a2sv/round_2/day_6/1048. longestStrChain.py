from typing import List


class Solution:
    # O(M*N) time and O(N) space where M is length of the longest string in words and N is the number of strings in words
    def longestStrChain(self, words: List[str]) -> int:
        wordset = set(words)
        memo = {}

        def dfs(s):
            if s not in wordset:
                return 0
            if s in memo:
                return memo[s]
            res = 0
            for i in range(len(s)):
                cur = s[:i] + s[i + 1:]
                if cur != s:
                    res = max(res, 1 + dfs(cur))
            memo[s] = res
            return memo[s]

        ret = 0
        for word in words:
            ret = max(ret, dfs(word))

        return ret
