def removeDuplicates(nums):

    numset = set(nums)
    index = 0
    length = len(numset)
    for i in range(length):
        nums[index] = min(numset)
        numset.remove(nums[index])
        index += 1
    return length

def removeDuplicates(nums):

    s = set(nums)
    l = len(s)
    j = 0
    for i in range(l):
        nums[j] = min(s)
        s.remove(nums[j])
        j += 1
    print(nums[:l])
    return l


print(removeDuplicates([-3,-3,-2,-1,-1,0,0,0,0,0]))
print(removeDuplicates([-3,-3,-3,-2,-1,-1,0,0,0,0,0]))
print(removeDuplicates([-3,-3,-2,-2,-2,-1,0,0,0,0,3,3]))
print(removeDuplicates([1,1,2]))
print(removeDuplicates([-1,0,0,0,0,3,3]))
print(removeDuplicates([1,1,1]))         
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))          
            




    
