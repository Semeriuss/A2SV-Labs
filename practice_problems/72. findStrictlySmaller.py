def findStrictlySmaller(nums, target):
    
    lower = 0
    upper = len(nums)
    
    best = -1
    while lower <= upper:
        mid = (lower + upper)//2
        if nums[mid] < target:
            best = mid
            lower = mid + 1 
        
        else:
            upper = mid - 1 
    return best

nums = [1, 2, 3, 5, 8, 12]
target = 5
print(findStrictlySmaller(nums, target))