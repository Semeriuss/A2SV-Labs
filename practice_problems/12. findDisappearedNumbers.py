# return unincluded numbers using hashet 
def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    
    # if there's no duplicate or missing number
    if len(set(nums)) == len(nums): return []

    # return symmetric difference of a complete set and set of given list
    return list(set(range(1, len(nums)+1))-set(nums))

# using in-place list element flagging method
def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    # [1,1]
    # [4,3,2,7,8,2,3,1] original list ->
    # [-4,-3,-2,-7,8,2,-3,-1] after first loop ->
    # only positive nums left in array[8 (i = 4), 2 (i = 5)] ->
    # return [5,6], the unincluded elements

    for num in nums:
        index = abs(num)    # if there's a negative number in original list
        if nums[index-1] > 0:    # if element at index is positive 
            nums[index-1] = -1*nums[index-1] # flag it, i.e., exists

    result = []
    for i in range(len(nums)):
        if nums[i] > 0:
            result.append(i+1)
    return result



tests = [[4,3,2,7,8,2,3,1],[1,1],[1,2]]
for test in tests:
    print(findDisappearedNumbers(test))
