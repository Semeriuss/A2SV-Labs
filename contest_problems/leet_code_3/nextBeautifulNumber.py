import collections


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:

        def isNumericallyBalanced(num):
            digits = list(str(num))
            digitsCount = collections.Counter(digits)
            return all(digitCount == int(digit) for digit, digitCount in digitsCount.items())
            
        nextNumber = n + 1
        while not isNumericallyBalanced(nextNumber):
            nextNumber += 1
        return nextNumber

tests = [1, 1000, 3000]
for test in tests:
    print(Solution().nextBeautifulNumber(test))
