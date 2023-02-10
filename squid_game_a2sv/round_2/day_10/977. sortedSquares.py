from typing import List


class Solution:
    # O(N) time | O(N) space
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[0] >= 0:
            return [num ** 2 for num in nums]

        res = []
        idx = None
        n = len(nums)
        for i, num in enumerate(nums):
            if num >= 0:
                idx = i
                break
        if idx is None:
            return [nums[i] ** 2 for i in range(n - 1, -1, -1)]

        i = idx - 1
        j = idx
        while i >= 0 and j < n:
            negsqr = nums[i]**2
            possqr = nums[j]**2
            if negsqr > possqr:
                res.append(possqr)
                j += 1
            elif negsqr < possqr:
                res.append(negsqr)
                i -= 1
            else:
                res.extend([negsqr, possqr])
                i -= 1
                j += 1

        while i >= 0:
            res.append(nums[i] ** 2)
            i -= 1

        while j < n:
            res.append(nums[j] ** 2)
            j += 1

        return res
