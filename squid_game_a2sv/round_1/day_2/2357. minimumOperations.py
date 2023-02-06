from typing import List
from collections import Counter


class Solution:
    # O(N) time, O(1) space
    def minimumOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ops = len(freq)
        ops -= 1 if freq[0] > 0 else 0
        return ops
