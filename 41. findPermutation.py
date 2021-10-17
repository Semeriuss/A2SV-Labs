def doPermute(listToPermute):

    n = len(listToPermute)
    
    if n == 1:
        return [listToPermute]


    permutations = []
           
    for i in range(n):
        staticVal = listToPermute[i]
        permutedList = doPermute(listToPermute[0:i] + listToPermute[i+1:])
        print(permutedList)
        for permuted in permutedList:
            merged = [staticVal]
            merged.extend(permuted)
            permutations.append(merged)
    return permutations
        

def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """    

    return doPermute(nums)

tests = [([1,2], [[1,2],[2,1]]),
         ([2], [[2]]),
         ([1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])]
for test in tests:
    nums, expected = test
    actual = permute(nums)
    print(actual == expected, "actual  ", actual, "expected", expected)
