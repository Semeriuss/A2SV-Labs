from typing import List


class Solution:
    def countArrangement(self, n: int) -> int:
        nums = list(range(1, n + 1))
        perms = self.permute(nums, 0, [])
        beautifulArrangements = 0
        for perm in perms:
            print(perm)
            if self.isBeautifulArrangement(perm):
                beautifulArrangements += 1
        return beautifulArrangements

    def isBeautifulArrangement(self, nums: List) -> bool:
        for i, num in enumerate(nums):
            if not (i + 1) % num or not num % (i + 1):
                continue
            return False
        return True
            
    def permute(self, nums: List, i: int , res: List) -> List:
        if i == len(nums):
            res.append(nums)
        else:
            perm = nums[:]
            for j in range(i, len(nums)):
                perm[i], perm[j] = perm[j], perm[i]
                self.permute(perm, i + 1, res)
        return res

print(Solution().countArrangement(3))