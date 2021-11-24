class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
            
        startPointer, endPointer = 0, 0
        def findPalindrome(s, sp, ep):
            nonlocal startPointer, endPointer
            while sp >= 0 and ep < len(s) and s[sp] == s[ep]:
                    ep += 1
                    sp -= 1   

            if endPointer < ep - sp - 1:
                startPointer = sp + 1
                endPointer = ep - sp - 1

        for i in range(len(s) - 1):
            findPalindrome(s, i, i)
            findPalindrome(s, i, i + 1)
            
        return s[startPointer: startPointer + endPointer]



s = "babad"
# s= "cbbd"
# s = "a"
# s = "ac"
# s = "cbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbd"
# print(len(s))
s = "cbcbbdacabcbbdacacaccabcabcadcaacacadcbbdacaacbbdacaccbbdacaacbbdacacbbcbbdacadcbbdacaacaca"

print(Solution().longestPalindrome(s))
