from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.result = []
        def findSum(target, res, index, memo):
            if (target, index) in memo and memo[(target, index)] == 0:
                self.result.append(memo[(target, index)])

            if target == 0:
                memo[(target, index)] = res
                self.result.append(memo[(target, index)])

            if target < 0 or index >= len(candidates):
                memo[(target, index)] = None
                return None

            for i in range(index, len(candidates)):
                memo[(target, index)] = findSum(target - candidates[i], res + [candidates[i]], i, memo)     

        findSum(target, [], 0, {})
        return self.result

nums = [2, 3]
target = 12
print(Solution().combinationSum(nums, target))