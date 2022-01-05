from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tally = sum(nums)
        for i, num in enumerate(nums):
            if (tally - num) % 3 != 0:
                nums[i] = -nums[i]
        print(nums)
        for num in nums:
            if num > 0:
                return num
        
        return 0