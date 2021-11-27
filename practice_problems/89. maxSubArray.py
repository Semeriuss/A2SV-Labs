def maxSubArraySum(nums):
    for i in range(1, len(nums)):
        nums[i] = max(nums[i], nums[i - 1])
    return max(nums)

nums = [-2,-3,4,5,1,-44,132,23]
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [1]
# nums = [5,4,-1,7,8]
# nums = [5,4,-1,7,8,-2,1,-3,4,-1,2,1,-5,4]
# nums = [-1]
# nums = [-2, 1]
# nums = [-2,-1,6]
print(maxSubArraySum(nums))