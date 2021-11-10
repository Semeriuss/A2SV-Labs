

def longestMountain(nums):
    length = currLength = 0
    goingDown = False

    # l = 0, cl = 4, i = 4, nums[i] = 3, nums[i + 1] = 2, gd = True
    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1] and not goingDown:
            currLength += 1
        
        elif currLength > 0 and nums[i] > nums[i + 1]:
            currLength += 1
            goingDown = True
            
        else:
            length = max(length, currLength)
            currLength = 0
        
    return length

nums = [2, 1, 4, 7, 3, 2, 5]
# nums = [2, 2, 2]
print(longestMountain(nums))