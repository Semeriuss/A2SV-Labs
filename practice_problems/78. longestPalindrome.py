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


s = "babad"
s= "cbbd"
s = "a"
s = "ac"
s = "cbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdcbbdbbdcbbdcbbdcbbdcbbdcbbdcbbd"
print(len(s))

print(Solution().longestPalindrome(s))
