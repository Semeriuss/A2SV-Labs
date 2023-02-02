from typing import List


class Solution:
    # O(N^2) time, O(1) space
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        zero_count = nums.count(0)
        positive_count = n - zero_count

        res = 0
        while positive_count > 0:
            res += 1
            x = 1000
            for num in nums:
                if num > 0 and num < x:
                    x = num

            for i in range(len(nums)):
                if nums[i] > 0:
                    nums[i] -= x
                    if nums[i] == 0:
                        positive_count -= 1

        return res
