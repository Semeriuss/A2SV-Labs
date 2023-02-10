from typing import List


class Solution:
    # O(N^2) time | O(1) space
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = 0
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    count += 1
                if nums[j] + nums[i] == target:
                    count += 1
        return count
