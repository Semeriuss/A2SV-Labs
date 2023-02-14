class Solution:
    # O(n) time and space
    def reorderedPowerOf2(self, n: int) -> bool:

        twos = set([])
        num = 1
        while num <= 10**9:
            twos.add(tuple(sorted(list(str(num)))))
            num *= 2

        digits = tuple(sorted(list(str(n))))
        return digits in twos
