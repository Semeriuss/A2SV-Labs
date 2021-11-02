from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        
        for i in range(n-1, -1, -1):
            currentMax = nums[i]
            credit = k
            currIndex = 0
            count = 1
            max_count = 1
            # if max_count > len(nums[:i]): return max_count
            while credit > 0 and currIndex <= i:
                credit -= (currentMax - nums[currIndex])
                if credit >= 0:
                    count += 1
                    currIndex += 1
            max_count = max(count, max_count)
        
        return max_count + 1

nums = [1, 2, 4]
k = 5
nums = [3,9,6]
k = 2
nums = [1,4,8,13]
k = 5
print(Solution().maxFrequency(nums,k))


                