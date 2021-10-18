def checkSubarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """

    #k = 6
    #nums = [23, 2, 4, 6, 7], i = 1
    for i in range(0, len(nums) - 1):
        index = 0
        currentSum = nums[i]

        #j = 2, currentSum = 6
        for j in range(i+1, len(nums)):
            currentSum += nums[j]

            if currentSum % k == 0:
                return True
            
    return False


print(checkSubarraySum([23, 2, 4, 6, 7], 13))
        