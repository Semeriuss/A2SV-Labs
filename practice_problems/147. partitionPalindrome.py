from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def subset(A):
            if A == []:
                return [[]]
            sub = subset(A[:-1])
            return sub + [rem + [A[-1]] for rem in sub]
        
        def isPalindrome(s):
            sp, ep = 0, len(s) - 1
            while sp < ep:
                if s[sp] != s[ep]:
                    return False
                sp += 1
                ep -= 1
            return True

        
        partitions, palindromes = subset(list(s))[1:], []
        for partition in partitions:
            if isPalindrome(partition):
                palindromes.append("".join(partition))
        return palindromes

s = "aab"
s = "a"
print(Solution().partition(s))