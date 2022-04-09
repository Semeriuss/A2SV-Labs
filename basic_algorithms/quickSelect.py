from random import random, randint
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def quickSelect(l, r, k):
            def partition(left, right, pindex):
                pivot = nums[pindex]
                nums[right], nums[pindex] = nums[pindex], nums[right]
                pindex = left
                for i in range(left, right):
                    if nums[i] <= pivot:
                        nums[pindex], nums[i] = nums[i], nums[pindex]
                        pindex += 1
                nums[pindex], nums[right] = nums[right], nums[pindex]
                return pindex
            if l == r:
                return nums[l]
            pivotIndex = randint(l, r)
            p = partition(l, r, pivotIndex)
            if p > k:
                return quickSelect(l, p - 1, k)
            elif p < k:
                return quickSelect(p + 1, r, k)
            else:
                return nums[p]
            
        return quickSelect(0, len(nums) - 1, len(nums) - k)
