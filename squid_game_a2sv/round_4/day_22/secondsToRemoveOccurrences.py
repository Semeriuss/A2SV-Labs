class Solution:
    # O(N^2) time and O(N) space
    def secondsToRemoveOccurrences(self, s: str) -> int:
        digits = list(s)
        res = 0
        changed = True
        while changed:
            changed = False
            i = 0
            while i < len(s) - 1:
                if digits[i] == '0' and digits[i + 1] == '1':
                    digits[i], digits[i + 1] = '1', '0'
                    changed = True
                    i += 2
                else:
                    i += 1
            if changed:
                res += 1
        return res
