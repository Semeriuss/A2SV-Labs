

def longestMountain(nums):
    length = 0

    sp = ep = 0
    goingDown = False

    # l = 0, sp = 0, ep = 3, nums[ep] = 7, nums[ep + 1] = 3
    while ep < len(nums) - 1:
        if nums[ep] > nums[ep + 1]:
            length = max(length, ep - sp)
            if not goingDown:
                sp = ep
        elif length > 0 and nums[ep] > nums[ep + 1]:
            goingDown = True

        ep += 1        
    return length

nums = [2, 1, 4, 7, 3, 2, 5]
# nums = [2, 2, 2]
print(longestMountain(nums))