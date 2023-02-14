from typing import List


class Solution:
    # O(n) time | O(n) space
    def sumZero(self, n: int) -> List[int]:
        if n % 2 == 1:
            return [0] + [i for i in range(1, n//2 + 1)] + [-i for i in range(1, n//2 + 1)]
        else:
            return [i for i in range(1, n//2 + 1)] + [-i for i in range(1, n//2 + 1)]
