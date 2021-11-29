from collections import defaultdict
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def hasPath(src, dst, memo):
            print(memo)
            pos, val = src
            if pos in memo:
                return memo
            if pos >= dst:
                memo[pos] = True
                return True
            if val == 0:
                memo[pos] = False
                return False
            for i in range(1, val + 1):
                memo[pos] = hasPath((pos + i, nums[pos + i]), dst, memo)
                print("I'm here", memo[pos])
                if memo[pos]:
                    print(pos, val, memo[pos])
                    return True
            memo[pos] = False
            return False
        
        def hasPath(src, dst, memo):
            stack = []
            stack.append(src)
            while stack:
                # print(stack)
                currPos, currVal = stack.pop()
                if currPos in memo and memo[currPos]:
                    return True
                if currPos >= dst:
                    memo[currPos] = True
                    return True
                for i in range(currVal, 0, -1):
                    if currPos + i <= len(nums) - 1:
                        stack.append((currPos + i, nums[currPos + i]))
                memo[currPos] = False
            return False
        return hasPath((0, nums[0]), len(nums) - 1, {})

# nums = [2, 3, 1, 1, 4]
# nums = [3,2,1,0,4]
# nums = [2, 0]
# nums = [2, 5, 0, 0]
# nums = [2, 5, 0, 0, 0, 0, 0, 0]
nums = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
print(Solution().canJump(nums))