from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
    
        def isPalindrome(s):
            sp, ep = 0, len(s) - 1
            while sp < ep:
                if s[sp] != s[ep]:
                    return False
                sp += 1
                ep -= 1
            return True

        palindromes = [list(s)] 
        for p in range(1, len(s)):
            partition = []
            for i in range(p):
                partition.append()
                if isPalindrome(s[:i+1]) and isPalindrome(s[i+1:]):
                    palindromes.append([s[:i+1], s[i+1:]])
        return palindromes


s = "aab"
s = "a"
s = "baa"
print(Solution().partition(s))