from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        self.minlen = float("inf")
        
        prefixsum = [0]
        for i, num in enumerate(nums):
            prefixsum.append(prefixsum[i] + num)
        
        def findMinSub(sp, ep, arr, k, dp):
            if (sp, ep) in dp: return dp[(sp, ep)]
            if sp > ep or ep < 0 or ep >= len(arr) or sp < 0 or sp >= len(arr):
                dp[(sp, ep)] = -1
                return 
            
            if arr[ep] - arr[sp] >= k:
                dp[(sp, ep)] = ep - sp
                self.minlen = min(self.minlen, ep - sp)
            
            dp[(sp, ep)] = findMinSub(sp + 1, ep, arr, k, dp)
            dp[(sp, ep)] = findMinSub(sp, ep - 1, arr, k, dp)
            
        
        findMinSub(0, len(prefixsum) - 1, prefixsum, k, {})

        return self.minlen if self.minlen != float("inf") else -1