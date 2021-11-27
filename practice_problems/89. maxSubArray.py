def maxSubArraySum(nums):
    maxsum = nums[0]
    currsum = 0
    for num in nums:
        if currsum < 0:
            currsum = 0
        currsum += num
        maxsum = max(maxsum, currsum)
    return maxsum

nums = [-2,-3,4,5,1,-44,132,23]
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [1]
# nums = [5,4,-1,7,8]
# nums = [5,4,-1,7,8,-2,1,-3,4,-1,2,1,-5,4]
# nums = [-1]
# nums = [-2, 1]
# nums = [-2,-1,6]
print(maxSubArraySum(nums))