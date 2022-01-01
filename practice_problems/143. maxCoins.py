from typing import List
from functools import reduce
from operator import __mul__

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        balloons = [1] + nums + [1]
        self.res = 0
        def dfs(balloon, res):
            if len(balloon) < 3:
                return balloon[1] * balloon[0]
            print(self.res, res, balloon)
            for i in range(1, len(balloon)):
                tempV, tempB = self.burst(balloon, i)
                dfs(tempB, res + tempV)
                self.res = max(self.res, res)
            
            self.res = max(self.res, res)
            return res
        dfs(balloons, 0)
        return self.res

    
    def burst(self, balloons, indexToRemove):
        # if len(balloons) < 3: return balloons[1], [1, 1]
        res = reduce(__mul__, balloons[indexToRemove - 1: indexToRemove + 2])
        modified = balloons[:indexToRemove] + balloons[indexToRemove + 1:] 
        return res, modified

nums = [3,1,5,8]
nums = [4,6,7,1]
nums = [2,3,4,9,3,2]
nums = [2,3,4,9,3]
nums = [2,3,4,3]
nums = [2,3,2,3]
print(Solution().maxCoins(nums))

"""
[2,3,4,5,6,9,1,3,5,6,2,3,9,2,1,4,5,7]
[21,32,42,12,32,43,65,75,87,75,53,24,46,57,68,67]
"""