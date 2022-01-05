from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
    
        def isPalindrome(s, memo):
            if len(s) == 1: return True
            if s in memo: return memo[s]
            sp, ep = 0, len(s) - 1
            while sp < ep:
                if s[sp] != s[ep]:
                    memo[s] = False
                    return memo[s]
                sp += 1
                ep -= 1
            memo[s] = True
            return memo[s]
        
        def partition(s):          
            if len(s) == 0:
                yield []
            else:
                for p in range(1, len(s) + 1):
                    prefix, suffix = s[:p], s[p:]
                    for part in partition(suffix):
                        yield [prefix] + part

        partitions, palindromes = [*partition(s)], [] 
        memo = {}
        for part in partitions:
            isPalindromic = True
            for p in part:
                if not isPalindrome(p, memo):
                    isPalindromic = False
                    break
            if isPalindromic: palindromes.append(part)
        return palindromes


s = "aab"
s = "a"
s = "baa"
s = "aaabb"
print(Solution().partition(s))

