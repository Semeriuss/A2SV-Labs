from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
    
        def dfs(s, path, res):
            if not s:
                res.append(path[:])
                return
            for i in range(1, len(s)+1):
                if s[:i] == s[i-1::-1]:
                    path.append(s[:i])
                    dfs(s[i:], path, res)
                    path.pop()
            return res
        res = []
        dfs(s, [], res)
        return res

s = "aab"
s = "a"
s = "baa"
# s = "aaabb"
print(Solution().partition(s))

