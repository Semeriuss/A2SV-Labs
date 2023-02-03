#
# @lc app=leetcode id=528 lang=python3
#
# [528] Random Pick with Weight
#

# @lc code=start
import random
from typing import List


class Solution:

    # O(N) time and space
    def __init__(self, w: List[int]):
        self.w = w
        for i in range(1, len(w)):
            self.w[i] += self.w[i - 1]

    # O(logN) time and O(1) space
    def pickIndex(self) -> int:
        l, r = 0, len(self.w) - 1
        target = random.randint(1, self.w[-1])
        while l < r:
            mid = (l + r) // 2
            if self.w[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l

        # Your Solution object will be instantiated and called as such:
        # obj = Solution(w)
        # param_1 = obj.pickIndex()
        # @lc code=end
