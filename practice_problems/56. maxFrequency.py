from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        
        sp = 0
        ep = 0
        while k > (ep - sp + 1) * nums[ep]:
            k += nums[sp]
            if k < (ep - sp + 1) * nums[ep]:
                k -= nums[sp]
                sp += 1
            ep += 1            
        return ep - sp + 1
        

nums = [1, 2, 4]
k = 5
nums = [3,9,6]
k = 2
nums = [1,4,8,13]
k = 5
nums = [3,9,6]
k = 3
print(Solution().maxFrequency(nums,k))


                