from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        sp, ep = 0, len(height) - 1
        maxContainer = 0
        while sp < ep:
            maxContainer = max(maxContainer, (ep - sp) * min(height[ep], height[sp]))
            if height[sp] < height[ep]:
                sp += 1
            else:
                ep -= 1
        return maxContainer


height = [1,8,6,2,5,4,8,3,7]
# height = [1,1]
# height = [4,3,2,1,4]
# height = [1,2,1]
# height = [2, 1, 2, 1]
# height = [3, 9, 3, 4, 7, 2, 12, 6]
print(Solution().maxArea(height))
        
        