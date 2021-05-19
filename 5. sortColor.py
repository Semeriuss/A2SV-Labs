def sort(nums):

    if len(nums) > 1:
        next_zero = 0
        next_two = len(nums)-1

        i = 0
        while(i <= next_two):
            if nums[i] == 0:
                nums[i], nums[next_zero] = nums[next_zero], nums[i]
                next_zero += 1
                i += 1

            elif nums[i] == 2:
                nums[i], nums[next_two] = nums[next_two], nums[i]
                next_two -= 1
                

            else:
                i += 1
            
    return nums

lst = [0]

print(sort(lst))
