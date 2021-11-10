def findPosition(nums, target, isFirst = False):

    lower = 0
    upper = len(nums) - 1
    best = -1

    while lower <= upper:
        mid = (lower + upper)//2
        if nums[mid] < target:
            lower = mid + 1
        
        elif nums[mid] > target:
            upper = mid - 1
        
        else:
            lower = lower if isFirst else mid + 1
            upper = mid - 1 if isFirst else upper
            best = mid
    
    return best
def searchRange(nums, target):
    first = findPosition(nums, target, True)
    if first == -1: return [-1, -1]
    return [first, findPosition(nums, target, False)]

nums = [5,7,7,8,8,10]
target = 8

nums = [5,7,7,8,8,10]
target = 6

nums = []
target = 0
print(searchRange(nums, target))