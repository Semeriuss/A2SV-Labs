def assertExpectedEqualsActual(expected, actual):
    return expected == actual

def findDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numSet = set()
        duplicates = []
        for num in nums:
            if num in numSet:
                duplicates.append(num)
            else:
                numSet.add(num)
        return duplicates

def findDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        duplicates = []

        for num in nums:
            num = abs(num)
            if nums[num-1] < 0:
                duplicates.append(num)
            nums[num-1] = -nums[num-1]

        return duplicates

tests = [([4,3,2,7,8,2,3,1], [2,3]), ([1,1,2],[1]), ([1],[])]
for test in tests:
    inputList, expected = test
    actual = findDuplicates(inputList)
    print(actual, expected)
    print(assertExpectedEqualsActual(expected, actual))
    

        
