from typing import List
from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1: return nums[0]
        reordered_nums = tuple([nums[-1]] + nums[:-1])
        @lru_cache(None)
        def dfs(index, houses):
            if index >= N: return 0
            return max(houses[index] + dfs(index + 2, houses), dfs(index + 1, houses))
        
        return dfs(0, reordered_nums)

nums = [9, 1, 4, 9, 1, 0]
nums = [1, 2, 3, 4, 5]
print(Solution().rob(nums))