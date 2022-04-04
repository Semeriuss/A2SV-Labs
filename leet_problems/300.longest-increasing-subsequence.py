#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        temp = [nums[0]]
        for num in nums:
            pos = bisect_left(temp, num)
            if pos == len(temp):
                temp.append(num)
            elif temp[pos] > num:
                temp[pos] = num
        return len(temp)
        
# @lc code=end

