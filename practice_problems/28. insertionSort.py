def insertionSort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i-1
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j + 1] = key                

    return nums

tests = [[1,2,5,2,1],[2,5,8,1,5,7]]
for test in tests:
    print(insertionSort(test))
