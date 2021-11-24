class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
            
        self.startPointer, self.endPointer = 0, 0
        def findPalindrome(s, sp, ep):
            while sp >= 0 and ep < len(s) and s[sp] == s[ep]:
                    ep += 1
                    sp -= 1   

            if self.endPointer < ep - sp - 1:
                self.startPointer = sp + 1
                self.endPointer = ep - sp - 1

        for i in range(len(s) - 1):
            findPalindrome(s, i, i)
            findPalindrome(s, i, i + 1)
            
        return s[self.startPointer: self.startPointer + self.endPointer]



s = "babad"
# s= "cbbd"
# s = "a"
# s = "ac"
# s = "cbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbd"
# print(len(s))
s = "cbcbbdacabcbbdacacaccabcabcadcaacacadcbbdacaacbbdacaccbbdacaacbbdacacbbcbbdacadcbbdacaacaca"

print(Solution().longestPalindrome(s))
