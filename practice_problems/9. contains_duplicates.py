def contains_duplicates(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    return len(set(nums))<len(nums)

tests = [[1,2,3,1],[1,2,3,4]]
for test in tests:
    print(contains_duplicates(test))
