from typing import List
import heapq
from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minD, maxD = deque(), deque()
        
        i = 0
        
        for num in nums:
            while maxD and num > maxD[-1]: maxD.pop()
            while minD and num < minD[-1]: minD.pop()

            maxD.append(num)
            minD.append(num)

            if maxD[0] - minD[0] > limit:
                if nums[i] == maxD[0]: maxD.popleft()
                if nums[i] == minD[0]: minD.popleft()

                i += 1
        
        return len(nums) - i