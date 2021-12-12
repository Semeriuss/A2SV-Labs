from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum, finalsum = 0, float("-inf")
        for num in nums:
            if num > num + maxsum:
                maxsum = num
            else:
                maxsum += num
            finalsum = max(maxsum, finalsum)
        return finalsum

    def maxSubArray(self, nums: List[int]) -> int:
        currsum, finalsum = nums[0], 0
        for num in nums:
            if currsum < 0:
                currsum = 0
            currsum += num
            finalsum = max(finalsum, currsum)
        return finalsum