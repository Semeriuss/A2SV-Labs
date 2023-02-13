from collections import defaultdict
from typing import List


class Solution:
    # O(N) time and O(N) space
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        totalSum = cummulativeSum = 0
        sums = defaultdict(int)
        for num in nums:
            cummulativeSum += num
            sums[cummulativeSum % k] += 1

        for k, v in sums.items():
            if k == 0:
                totalSum += v + (v * (v - 1))//2
            else:
                totalSum += (v * (v - 1))//2

        return totalSum
