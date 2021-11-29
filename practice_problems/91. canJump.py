from collections import deque
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        self.res = False
        def hasPath(pos, visited):
            if pos >= len(nums) - 1:
                self.res = True
                return self.res
            
            if len(visited) == len(nums):
                return 
            visited.add(pos)
            for i in range(1, nums[pos] + 1):
                if i >= len(nums) - 1:
                    self.res = True
                    return True
                if i not in visited and hasPath(i, visited):
                    self.res = True
                    return True
            self.res = False
            return self.res
        return hasPath(0, set())

        def hasPath(src):
            queue = deque()
            visited = set()
            queue.append(src)
            visited.add(src)
            while queue:
                currPos = queue.popleft()
                maxJump = currPos + nums[currPos] + 1              
                for i in range(currPos + 1, maxJump):
                    if i >= len(nums):
                        return True
                    if i not in visited and i < len(nums):
                        visited.add(i)
                        queue.append(i)
            return False
        return hasPath(0)

nums = [2, 3, 1, 1, 4]
# nums = [3,2,1,0,4]
# nums = [2, 0]
# nums = [2, 5, 0, 0]
# nums = [2, 5, 0, 0, 0, 0, 0, 0]
# nums = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
print(Solution().canJump(nums))