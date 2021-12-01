from typing import List
from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1: return nums[0]
        @lru_cache(None)
        def dfs(src):
            if src >= N:
                return 0
            return max(nums[src] + dfs(src + 2), dfs(src + 1))
        
        return dfs(0)

nums = [9, 1, 2, 9]
nums = [9, 1, 4, 9, 1, 0]
nums = [1, 2, 3, 1]
nums = [2,7,9,3,1]
nums = [2,7,9,3,1,2,7,9,3,1,2,7,9,3,1,2,7,9,3,1,2,7,9,3,1,2,7,9,3,1,2,7,9,3,1,2,7,9,3,1,2,7,9,3,1,2,7,9,3,1,2,7,9,3,1,2,7,9,3,1,2,7,9,3,1]
print(len(nums))
print(Solution().rob(nums))
            
        