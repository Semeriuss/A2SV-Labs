from typing import List


class Solution:
    # O(n) time and O(1) space
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum, finalsum = 0, float('-inf')
        for num in nums:
            if num > num + maxsum:
                maxsum = num
            else:
                maxsum += num
            finalsum = max(finalsum, maxsum)
        return finalsum
