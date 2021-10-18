def checkPossibility(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    count = 0    
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            count += 1
            if (i-2 < 0) or (nums[i-2] <= nums[i]):
                nums[i-1] = nums[i]
        else:
            nums[i] = nums[i-1]
        print(nums, count)
    
    if count > 1:
        return False
    return True

tests = [[4,2,3],[4,2,1]]
for test in tests:
    print(checkPossibility(test))
