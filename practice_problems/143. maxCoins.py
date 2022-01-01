from typing import List
from functools import reduce
from operator import __mul__

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        balloons = [1] + nums + [1]
        self.res = 0
        def dfs(b):
            if len(b) < 3:
                return 0

            first, firstB = self.burst(b, 1)
            second, secondB = self.burst(b, 2)
            # self.res += max(first, second)
            # print(firstB, secondB, b, first, second, self.res)
            # dfs(firstB) if first > second else dfs(secondB)
            return max(first + dfs(firstB), second + dfs(secondB))
        return dfs(balloons)
        # return self.res
    
    def burst(self, balloons, indexToRemove):
        if len(balloons) < 3: return balloons[0] * balloons[1]
        res = reduce(__mul__, balloons[indexToRemove - 1: indexToRemove + 2])
        modified = balloons[:indexToRemove] + balloons[indexToRemove + 1:] 
        return res, modified

nums = [3,1,5,8]
nums = [4,6,7,1]
print(Solution().maxCoins(nums))

