def removeDuplicates(nums):

    numset = sorted(set(nums))
    j = 0
    for i in numset:
        nums[j] = i
        j += 1
    print(nums)
    return len(numset)


print(removeDuplicates([1,1,2]))
print(removeDuplicates([1,1,2,3]))
print(removeDuplicates([1,1,1]))         
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))          
            




    
