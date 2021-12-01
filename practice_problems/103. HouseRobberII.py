from typing import List
from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1: return nums[0]
        @lru_cache(None)
        def dfs(index, houses, BOUND):
            if index >= BOUND: return 0
            return max(nums[index] + dfs(index + 2, houses, BOUND), dfs(index + 1, houses, BOUND))
            
        houses = tuple(nums)
        return max(dfs(1, houses, N), dfs(0, houses[:-1], N - 1))

nums = [9, 1, 4, 9, 1, 0]
nums = [1, 2, 3, 4, 5]
nums = [9, 1, 4, 9, 1, 0,1, 2, 3, 4, 5,1, 2, 3, 4, 5, 9, 1, 4, 9, 1, 9, 1, 4, 9, 1, 0,1, 2, 3, 4, 5,1, 2, 3, 4, 5, 9, 1, 4, 9, 1, 0,1, 2, 3, 4, 5,1, 2, 3, 4, 5,1, 2, 3, 4, 5, 9, 1, 4, 9, 1, 0,1, 2, 3, 4, 5,1, 2, 3, 4, 5,1, 2, 3, 4, 5, 9, 1, 4, 9, 1, 0,1, 2, 3, 4, 5,1, 2, 3, 4, 5,1, 2, 3, 4, 5, 1, 2, 3, 4, 5,]
print(len(nums))
print(Solution().rob(nums))