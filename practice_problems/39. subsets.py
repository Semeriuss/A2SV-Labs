def parse(nums):
    n = len(nums)

    subsets = []
    
    if n == 1:
        return [nums]

    for i in range(n):
        subsets.append(
        if [nums[i]] not in subsets:
            subsets.append([nums[i]])

        remainingList = nums[0:i] + nums[i+1:]
            
        

        print(remainingList, "rrr")
            
    return subsets        

    
def subsets(nums):
    finalList = [[]]
    finalList.extend(parse(nums))
    return finalList

test = [1, 2]
print(subsets(test))

##tests = [([1, 2, 3], [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]),
##         ([0], [[],[0]])]
##
##for test in tests:
##    nums, expected = test
##    actual = subsets(nums)
##    print(actual == expected, "E => ", expected, "A=> ", actual)
