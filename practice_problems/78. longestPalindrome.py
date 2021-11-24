from collections import deque
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(sp, ep):
            while sp < ep:
                if s[sp] != s[ep]:
                    return False
                sp += 1
                ep -= 1
            return True

        ans = ""
        for i in range(len(s)):
            for j in range(len(s) - 1, i - 1, -1):
                if isPalindrome(i, j):
                    ans = s[i : j + 1] if len(s[i : j + 1]) >= len(ans) else ans
                    break
        return ans

    def longestPalindrome(self, s: str) -> str:
        ans = ""
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))] 
        for i in range(len(s)):
            dp[i][i] = True  
            ans = s[i]    

        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    if dp[i + 1][j - 1] or j - i == 1:
                        dp[i][j] = True
                        ans = s[i : j + 1] if len(s[i : j + 1]) >= len(ans) else ans
        return ans
    
    # def longestPalindrome(self, s: str) -> str:
    #     if len(s) < 2:
    #         return s
            
    #     startPointer, endPointer = 0, 0
    #     def findPalindrome(s, sp, ep):
    #         nonlocal startPointer, endPointer
    #         while sp >= 0 and ep < len(s) and s[sp] == s[ep]:
    #                 ep += 1
    #                 sp -= 1   

    #         if endPointer < ep - sp - 1:
    #             startPointer = sp + 1
    #             endPointer = ep - sp - 1

    #     for i in range(len(s) - 1):
    #         findPalindrome(s, i, i)
    #         findPalindrome(s, i, i + 1)
            
    #     return s[startPointer: startPointer + endPointer]



s = "babad"
# s= "cbbd"
# s = "a"
# s = "ac"
# s = "cbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbd"
# print(len(s))
s = "cbcbbdacabcbbdacacaccabcabcadcaacacadcbbdacaacbbdacaccbbdacaacbbdacacbbcbbdacadcbbdacaacaca"

print(Solution().longestPalindrome(s))
