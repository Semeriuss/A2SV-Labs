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
        
        def partition(s):
            for p in range(len(s)):
                prefix, suffix = s[:p+1], s[p+1:]
                for part in partition(suffix):
                    yield [prefix] + part
            

                



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
# print(Solution().partition(s))

def partition(s):
    for p in range(1, len(s)+1):
        if len(s) > 0:
            prefix, suffix = s[:p], s[p:]
            for part in partition(suffix):
                yield [prefix] + part
    else:
        yield []

y = [*partition("12")]
print(y)