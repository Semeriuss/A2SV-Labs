from typing import List

def maxSumTwoNoOverlap(nums: List[int], firstLen: int, secondLen: int) -> int:
    if len(nums) < firstLen + secondLen: return 0
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    
    res, maxFirst, maxSecond = nums[firstLen + secondLen - 1], nums[firstLen - 1], nums[secondLen - 1]
    for i in range(firstLen + secondLen, len(nums)):
        maxFirst = max(maxFirst, nums[i - secondLen] - nums[i - secondLen - firstLen])
        maxSecond = max(maxSecond, nums[i - firstLen] -  nums[i - secondLen - firstLen])
        res = max(res, maxFirst + nums[i] - nums[i - secondLen], maxSecond + nums[i] - nums[i - firstLen])
    return res
    

        

tests = [([0,6,5,2,2,5,1,9,4], 1, 2), 
        ([3,8,1,3,2,1,8,9,0], 3, 2), 
        ([2,1,5,6,0,9,5,0,3,8], 4, 3),
        ([0,6,5,2,2,5,1,9,4], 1, 2),
        ([3,8,1,3,2,1,8,9,0], 3, 2),
        ([2,1,5,6,0,9,5,0,3,8], 4, 3),
        ([0,6,5,2,2,5,1,9,4], 3, 2),
        ([3,8,1,3,2,1,8,9,0], 4, 3)]

tests = [([8,20,6,2,20,17,6,3,20,8,12], 5, 4)]
for test in tests:
    nums, firstLen, secondLen = test
    print(maxSumTwoNoOverlap(nums, firstLen, secondLen))



