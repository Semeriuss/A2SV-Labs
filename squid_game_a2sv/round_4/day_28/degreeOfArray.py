from collections import Counter
from typing import List


class Solution:
    # O(N*2) time and O(N) space
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = Counter(nums)
        mx = max(freq.values())
        vals = set([num for num in nums if freq[num] == mx])
        n = len(nums)
        if mx == 1:
            return 1
        res = n
        for val in vals:
            temp = 1
            start = None
            for i, num in enumerate(nums):
                if start is None and num == val:
                    start = i
                elif num == val:
                    temp = max(temp, i - start + 1)
            res = min(temp, res)
        return res
