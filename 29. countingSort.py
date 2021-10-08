def countSort(nums):
    maxNum = int(max(nums))
    minNum = int(min(nums))
    rangeOfNums = maxNum - minNum + 1

    count_arr = [0 for _ in range(rangeOfNums)]
    sortedNums = [0 for _ in range(len(nums))]


    for i in range(len(nums)):
        count_arr[nums[i] - minNum] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]

    for i in range(len(nums)-1, -1, -1):
        sortedNums[count_arr[nums[i] - minNum] - 1] = nums[i]
        count_arr[nums[i] - minNum] -= 1

    for i in range(0, len(nums)):
        nums[i] = sortedNums[i]

    return nums

tests = [[-5, -10, 0, -3, 8, 5, -1, 10]]
for test in tests:
    print(countSort(test))
