from typing import List
import heapq

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        sp, ep, maxlen = 0, 0, 0
        n = len(nums)
        maxV, minV = nums[sp], nums[ep]
        minheap, maxheap = [], []
        while ep < n:
            if maxV - minV <= limit:
                maxlen = max(maxlen, ep - sp + 1)
                ep += 1
                if ep >= n: break
                maxV = max(maxV, nums[ep])
                minV = min(minV, nums[ep])
                heapq.heappush(minheap, (nums[ep], ep))
                heapq.heappush(maxheap, (-nums[ep], ep))
            else:
                sp += 1
                if sp >= n: break
                if nums[sp - 1] == minV:
                    while minheap:
                        curr, ind = heapq.heappop(minheap)
                        if ind >= sp:
                            # sp = ind
                            minV = min(nums[ep], nums[sp], curr)
                            break
                elif nums[sp - 1] == maxV:
                    while maxheap:
                        curr, ind = heapq.heappop(maxheap)
                        if ind >= sp:
                            maxV = max(nums[sp], nums[ep], -curr)
                            break

        return maxlen