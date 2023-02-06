class Solution:
    def numberOfWays(self, s: str) -> int:
        ones = zeros = oneZeros = zeroOnes = oneZone = zeroOzero = 0
        for c in s:
            if c == '0':
                zeros += 1
                oneZeros += ones
                zeroOzero += zeroOnes
            else:
                ones += 1
                zeroOnes += zeros
                oneZone += oneZeros
        return oneZone + zeroOzero
