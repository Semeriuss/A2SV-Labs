from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        def findSum(target, res, index):
            if target == 0: self.result.append(res)
            if target < 0 or index >= len(candidates): return None
            for i in range(index, len(candidates)):
                findSum(target - candidates[i], res + [candidates[i]], i)     
        findSum(target, [], 0)
        return self.result
nums = [2, 3]
target = 12
print(Solution().combinationSum(nums, target))