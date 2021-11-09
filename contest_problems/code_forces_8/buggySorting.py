def buggySorting(n):
    
    nums = [i for i in range(n, 0, -1)]
    for i in range(0, n - 1):
        for j in range(i, n - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    
    print(nums)

buggySorting(2)

n = int(input())

def counterExample(n):
    sequence = [-1]

    if n == 1 or n == 2:
        return sequence
 
    return [i for i in range(n, 0, -1)]

print(*counterExample(n), sep=" ")
