class Solution:
    # O(n) time | O(n) space
    def validPalindrome(self, s: str, credit : int = 1) -> bool:
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] != s[end] and not credit:
                return False
            elif s[start] != s[end]:
                return self.validPalindrome(s[start:end], 0) or self.validPalindrome(s[start + 1: end + 1], 0)
            else:
                start += 1
                end -= 1
        return True
