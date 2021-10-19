def helper(nums, i):
    if i >= len(nums):
        return [[]]

    store = helper(nums, i + 1)
    temp = []
    for item in store:
        temp.append([nums[i]] + item)
        temp.append(item)
    return temp

def findSubs(i, sub, store, nums, n,visited):
    store.append(sub[:])
    for j in range(i + 1, n):
        if j not in visited:
            sub.append(nums[j])
            visited.add(j)
            findSubs(j, sub, store, nums, n,visited)
            sub.pop()
            visited.remove(j)
    return store
        
def subsets(nums):
    # return helper(nums, 0)

    store = [[]]
    n = len(nums)
    for i in range(n):
        findSubs(i, [nums[i]], store, nums, n,set([i]))
    
    return store

def getMaxBitwiseOr(nums):
    maxBitwiseOr = 0
    for num in nums:
        maxBitwiseOr |= num
    return maxBitwiseOr

def getSubsets(i, sub, store, nums, visited):
    store.append(sub[:])
    for j in range(i + 1, len(nums)):
        if j not in visited:
            sub.append(nums[j])
            visited.add(j)
            getSubsets(j, sub, store, nums, visited)
            sub.pop()
            visited.remove(j)
    return store

def getSubsetsHelper(nums, i):
    if i >= len(nums):
        return [[]]
    temp = getSubsetsHelper()

def countMaxOrSubsets(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maxBitwiseOr = getMaxBitwiseOr(nums)
    
    subsets = []
    for i in range(len(nums)):
        getSubsets(i, [nums[i]], subsets, nums, set([i]))
    # subsets = helper(nums, 0)

    print(subsets)
    count = 0
    for subset in subsets:
        if getMaxBitwiseOr(subset) == maxBitwiseOr:
            count += 1

    return count 

    

nums = [3,2,1,5]
nums = [2,2,2]
# nums = [3,1]

# print(subsets(nums))

print(countMaxOrSubsets([3,2,1,5]))