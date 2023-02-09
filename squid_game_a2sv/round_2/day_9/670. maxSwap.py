class Solution:
    # O(M) time and space where M is the number of digits in num
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        n = len(digits)
        for i in range(n - 1):
            front = digits[i]
            mx = front
            mxIdx = i
            for j in range(i + 1, n):
                if digits[j] >= mx:
                    mx = digits[j]
                    mxIdx = j
            if mx != front and i != mxIdx:
                digits[mxIdx], digits[i] = digits[i], digits[mxIdx]
                break
        return int("".join(digits))
