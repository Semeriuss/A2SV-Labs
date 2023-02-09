from collections import defaultdict
from typing import List


class Solution:
    # O(N) time and space
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def ksubs(k):
            res = left = 0
            count = defaultdict(int)
            for right, num in enumerate(nums):
                count[num] += 1
                while len(count) > k:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        count.popo(nums[left])
                    left += 1
                res += right - left
            return res

        return ksubs(k) - ksubs(k - 1)
