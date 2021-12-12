from typing import List


class Solution:
    def countArrangement(self, n: int) -> int:
        self.count = 0
        nums = list(range(1, n + 1))
        self.permuteAndCount(nums, 0, 0, False)
        return self.count


    def permuteAndCount(self, nums: List, i: int , count: int, beautifulOrder: bool) -> List:
        if i == len(nums):
            if beautifulOrder:
                self.count += 1
        else:
            perm = nums[:]
            for j in range(i, len(nums)):
                perm[i], perm[j] = perm[j], perm[i]
                if not (i + 1) % perm[i] or not perm[i] % (i + 1):
                    beautifulOrder = True
                    self.permuteAndCount(perm, i + 1, count, beautifulOrder)
        return count


print(Solution().countArrangement(15))