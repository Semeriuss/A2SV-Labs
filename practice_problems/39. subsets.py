def parse(i,sub,finalList,nums,n):
    finalList.append(sub[:])
    for j in range(i + 1,n):
        if nums[j] not in sub:
            # n_sub = sub[:]
            # n_sub.append(nums[j])
            sub.append(nums[j])
            parse(j,sub,finalList,nums,n)
            sub.pop()
    
def subsets(nums):
    finalList = []
    n = len(nums)
    for i in range(n):
        parse(i,[nums[i]],finalList,nums,n)
    
    return finalList

test = [1, 2,3]
print(subsets(test))

##tests = [([1, 2, 3], [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]),
##         ([0], [[],[0]])]
##
##for test in tests:
##    nums, expected = test
##    actual = subsets(nums)
##    print(actual == expected, "E => ", expected, "A=> ", actual)
