from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        ans = sorted([nums[i], nums[j], nums[k]])
                        if tuple(ans) not in visited:
                            visited.add(tuple(ans))
                            res.append(ans)
        return res
        