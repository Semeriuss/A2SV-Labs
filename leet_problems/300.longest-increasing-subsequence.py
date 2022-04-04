#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # print(len(nums))
        maxlen = 0
        for i, num in enumerate(nums):
            mark = num
            count = 1
            stack = [mark]
            j = i + 1
            while j < len(nums):
                if nums[j] > mark:
                    if stack[-1] >= nums[j]:
                        maxlen = max(maxlen, count)
                        print(stack)
                        while stack[-1] >= nums[j]:
                            stack.pop()
                            count -= 1
                    
                    stack.append(nums[j])
                    count += 1
                j += 1
            maxlen = max(maxlen, count)
        return maxlen

        
# @lc code=end

