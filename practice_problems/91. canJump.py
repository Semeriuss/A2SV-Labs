from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def hasPath(src, dst):
            if src == dst:
                return True
            if src == 0:
                return False
            for i in range(src):
                if hasPath(nums[i], dst):
                    return True
            return False
        
        def hasPath(src, dst):
            stack = []
            stack.append(src)
            while stack:
                print(stack)
                currPos, currVal = stack.pop()
                if currPos >= dst:
                    return True
                for i in range(1, currVal + 1):
                    if currPos + i <= len(nums) - 1:
                        stack.append((currPos + i, nums[currPos + i]))
            return False
        return hasPath((0, nums[0]), len(nums) - 1)

nums = [2, 3, 1, 1, 4]
nums = [3,2,1,0,4]
nums = [2, 0]
nums = [2, 5, 0, 0]
print(Solution().canJump(nums))