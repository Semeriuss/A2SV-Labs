class Solution:
    # O(N) time and space - N size of expected string
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            columnNumber -= 1
            div, mod = divmod(columnNumber, 26)
            res.append(chr(ord('A') + mod))
            columnNumber = div
        return "".join(res[::-1])
