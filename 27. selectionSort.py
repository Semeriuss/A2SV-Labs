def selectionSort(nums):
    for i in range(len(nums)):
        minIndex = i
        for j in range(i+1, len(nums)):
            if nums[minIndex] > nums[j]:
                minIndex = j

        nums[i], nums[minIndex] = nums[minIndex], nums[i]
                

    return nums

tests = [[1,2,5,2,1],[2,5,8,1,5,7]]
for test in tests:
    print(selectionSort(test))
