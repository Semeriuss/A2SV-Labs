#O(n^2) time, O(1) space
def twoSum(nums, target):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j] == target):
                return [i, j]

#O(n) time, O(1) space
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    numSet = set()
    doubleFlag = False
    targetList = []
    for num in nums:
        if num in numSet and num == target-num:
            doubleFlag = True
        numSet.add(target - num)

    for i, num in enumerate(nums):
        if not doubleFlag and num == target-num:
            continue
        if(num in numSet):
            targetList.append(i)

    print(numSet)

    return targetList


            
tests = [([2,7,11,15],9, [0,1]),
         ([3,2,4],6, [1,2]),
         ([3,3],6,[0,1]),
         ([0,2,4,1,3], 7, [2, 4]),
         ([-3,4,3,90], 0, [0,2])]

for test in tests:
    nums, target, expected = test
    actual = twoSum(nums, target)
    print(actual == expected, actual, expected)

