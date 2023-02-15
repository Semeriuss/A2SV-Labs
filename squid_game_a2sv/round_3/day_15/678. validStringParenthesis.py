class Solution:
    # O(N) time and O(1) space
    def checkValidString(self, s: str) -> bool:
        opener = closer = 0
        for c in s:
            if c == ')':
                opener -= 1
            else:
                opener += 1
            if opener < 0:
                return False

        for c in s[::-1]:
            if c == '(':
                closer -= 1
            else:
                closer += 1
            if closer < 0:
                return False
        return True
