from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = [""]
        for c in s:
            res = [x + cc for x in res for cc in {c, c.swapcase()}]
        return res
        
        

s= "a1b3d"
print(Solution().letterCasePermutation(s))
        