class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        dp = [None for _ in range(len(s))]
        ans = ""
        for j in range(len(s)):
            for i in range(j+1):
                if i == j:
                   dp[i] = True
                elif j == i + 1:
                    dp[i] = s[i] == s[j]
                else:
                    dp[i] = dp[i + 1] and s[i] == s[j]
                
                if dp[i] and j - i + 1 > len(ans):
                    ans = s[i : j + 1]
        return ans



s = "babad"
# s= "cbbd"
# s = "a"
# s = "ac"
# s = "cbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbd"
# print(len(s))
s = "cbcbbdacabcbbdacacaccabcabcadcaacacadcbbdacaacbbdacaccbbdacaacbbdacacbbcbbdacadcbbdacaacaca"

print(Solution().longestPalindrome(s))
