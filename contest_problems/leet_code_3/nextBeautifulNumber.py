import collections


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:

        def isNumericallyBalanced(num):
            digits = list(str(num))
            counts = collections.Counter(digits)

            return all(count == int(digit) for digit, count in counts.items())
            
        nextNumber = n + 1
        while not isNumericallyBalanced(nextNumber):
            nextNumber += 1
        return nextNumber

tests = [1, 1000, 3000]
for test in tests:
    print(Solution().nextBeautifulNumber(test))
