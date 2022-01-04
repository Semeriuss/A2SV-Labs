from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        self.res = []
        
        def permute(i, path):
            if i < len(s):
                if s[i].isalpha():
                    permute(i + 1, path + [s[i].upper()])
                    permute(i + 1, path + [s[i].lower()])
                
                else:
                    permute(i + 1, path + [s[i]])
            
            elif i == len(s):
                self.res.append("".join(path))
                return 
            else:
                return 
        
        permute(0, [])
        return self.res

s= "a1b3d"
print(Solution().letterCasePermutation(s))
        