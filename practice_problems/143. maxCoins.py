from typing import List
from functools import cache, reduce

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + [num for num in nums if num > 0] + [1]
        n = len(nums)

        @cache  
        def burst(i, j):
                return max([nums[i] * nums[k] * nums[j] + burst(i, k) + burst(k, j) for k in range(i + 1, j)] or [0]) 
        return burst(0, n - 1)

nums = [3,1,5,8]
nums = [4,6,7,1]
nums = [2,3,4,9,3,2]
nums = [2,3,4,9,3]
nums = [2,3,4,3]
nums = [2,3,2,3]
print(Solution().maxCoins(nums))

"""
[2,3,4,5,6,9,1,3,5,6,2,3,9,2,1,4,5,7]
[21,32,42,12,32,43,65,75,87,75,53,24,46,57,68,67]
"""