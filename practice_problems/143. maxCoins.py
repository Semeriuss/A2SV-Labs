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
            # print(firstB, secondB, b) #, first, second)
            # dfs(firstB) if first > second else dfs(secondB)
            f = first + dfs(firstB)
            print("f => ", firstB, "   ", f)
            s = second + dfs(secondB)
            print("s => ", secondB, "   ", s)
            third, thirdB = self.burst(b, 3)
            t = third + dfs(thirdB)
            return max(f, s, t)
        return dfs(balloons)
        # return self.res
    
    def burst(self, balloons, indexToRemove):
        if len(balloons) < 3: return balloons[1], [1, 1]
        res = reduce(__mul__, balloons[indexToRemove - 1: indexToRemove + 2])
        modified = balloons[:indexToRemove] + balloons[indexToRemove + 1:] 
        return res, modified

nums = [3,1,5,8]
nums = [4,6,7,1]
nums = [2,3,4,9,3,2]
nums = [2,3,4,9,3]
nums = [2,3,4,3]
print(Solution().maxCoins(nums))

"""
[2,3,4,5,6,9,1,3,5,6,2,3,9,2,1,4,5,7]
[21,32,42,12,32,43,65,75,87,75,53,24,46,57,68,67]
"""