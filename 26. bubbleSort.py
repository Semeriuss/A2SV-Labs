def bubbleSort(nums):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums

tests = [[1,2,5,2,1],[2,5,8,1,5,7]]
for test in tests:
    print(bubbleSort(test))
