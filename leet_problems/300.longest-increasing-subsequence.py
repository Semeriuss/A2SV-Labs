#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        self.maxlen = 1
        def dp(curmark, curpos, maxsofar):
            if N - curpos - 1 + maxsofar < self.maxlen:
                return
            if curpos >= N:
                self.maxlen = max(self.maxlen, maxsofar)
                return
            if nums[curpos] > curmark:
                dp(nums[curpos], curpos + 1, maxsofar + 1)
            dp(curmark, curpos + 1, maxsofar)

        i = 0
        while N - i - 1 >= self.maxlen:
            dp(nums[i], i, 1)
            i += 1
        return self.maxlen
        
# @lc code=end

