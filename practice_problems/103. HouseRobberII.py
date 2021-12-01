from typing import List
from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        def simple_rob(nums):
            prev, nex = 0, 0
            for money in nums: prev, nex = nex, max(prev + money, nex)
            return nex
        return max(nums[0], simple_rob(nums[:-1]), simple_rob(nums[1:]))

nums = [9, 1, 4, 9, 1, 0]
nums = [1, 2, 3, 4, 5]
nums = [9, 1, 4, 9, 1, 0,1, 2, 3, 4, 5,1, 2, 3, 4, 5, 9, 1, 4, 9, 1, 9, 1, 4, 9, 1, 0,1, 2, 3, 4, 5,1, 2, 3, 4, 5, 9, 1, 4, 9, 1, 0,1, 2, 3, 4, 5,1, 2, 3, 4, 5,1, 2, 3, 4, 5, 9, 1, 4, 9, 1, 0,1, 2, 3, 4, 5,1, 2, 3, 4, 5,1, 2, 3, 4, 5, 9, 1, 4, 9, 1, 0,1, 2, 3, 4, 5,1, 2, 3, 4, 5,1, 2, 3, 4, 5, 1, 2, 3, 4, 5,]
print(len(nums))
print(Solution().rob(nums))