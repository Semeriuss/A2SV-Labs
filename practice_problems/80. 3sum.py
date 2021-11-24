from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        N, res = len(nums), []
        for i in range(N):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            sp, ep = i + 1, N - 1
            target = nums[i] * -1
            while sp < ep:
                if nums[sp] + nums[ep] == target:
                    res.append([nums[i], nums[sp], nums[ep]])
                    sp += 1
                    while sp < ep and nums[sp] == nums[sp - 1]:
                        sp += 1
                
                elif nums[sp] + nums[ep] < target:
                    sp += 1
                
                else:
                    ep -= 1
            
        return res


test = [-1,0,1,0,2,-1,1,0,2,-1,1,0,2,-1,0,2,-4,-1,0,1,0,2]
test = [-1,0,1,2,-1,-4]
test = [0, 0]
print(Solution().threeSum(test))