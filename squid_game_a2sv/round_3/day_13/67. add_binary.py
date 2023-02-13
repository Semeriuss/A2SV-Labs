class Solution:
    # O(max(len(a), len(b))) time and O(max(len(a), len(b))) space
    def addBinary(self, a: str, b: str) -> str:
        res, carry = [], 0
        c, d = list(a), list(b)
        while c or d or carry:
            if c:
                carry += int(c.pop())
            if d:
                carry += int(d.pop())
            res.append(str(carry % 2))
            carry //= 2
        return "".join(res[::-1])
