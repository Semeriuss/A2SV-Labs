from typing import List


class Solution:
    # O(N) time and O(1) space
    def maximumDifference(self, nums: List[int]) -> int:
        mn = float('inf')
        res = -1
        for num in nums:
            res = max(num - mn, res)
            mn = min(mn, num)
        return res if res else -1
