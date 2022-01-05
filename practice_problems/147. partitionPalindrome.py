from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        def segment(s, path):
            if not s:
                self.res.append(path[:])
                return
            for i in range(len(s)):
                if s[:i+1] == s[i::-1]:
                    path.append(s[:i+1])
                    segment(s[i+1:], path)
                    path.pop()
        segment(s, [])
        return self.res
                

s = "aab"
s = "a"
s = "baa"
# s = "aaabb"
print(Solution().partition(s))

