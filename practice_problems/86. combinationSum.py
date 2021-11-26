from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def findSum(remaining, store):
            if remaining == 0: result.append(store)
            for item in candidates:
                if item > remaining: break
                if store and store[-1] > item: continue
                else: findSum(remaining - item, store + [item])
        findSum(target, [])
        return result
nums = [2, 3]
target = 12
print(Solution().combinationSum(nums, target))