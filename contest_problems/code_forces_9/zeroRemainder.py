def zeroRemainderArray(nums, k):
    
    numbersToModify = 0
    for i in range(len(nums)):
        if nums[i] % k != 0:
            numbersToModify += 1
    
    if numbersToModify == 0:
        return 0
    
    def foundDivisibleNumber(nums,x, k):
        found = False
        changedNum = 0
        for i in range(len(nums)):
            if nums[i] % k == 0:
                continue
            if (nums[i] + x) % k == 0:
                changedNum = nums[i] + x
                nums[i] += x
                found = True
                break
            
        if found: nums.remove(changedNum)
        return found

    x = 1
    while numbersToModify > 0:
        if foundDivisibleNumber(nums, x, k):
            numbersToModify -= 1
        x += 1
    
    return x

# tests = [([1, 2, 1, 3], 3), 
#         ([8, 7, 1, 8, 3, 7, 5, 10, 8, 9], 6), 
#         ([20, 100, 50, 20, 100500], 10),
#         ([24, 24, 24, 24, 24, 24, 24, 24, 24, 24], 25),
#         ([1, 2, 3, 4, 5, 6, 7, 8], 8)]

# for test in tests:
#     nums, k = test
#     print(zeroRemainderArray(nums, k))

if __name__ == "__main__":
    t = int(input())
    res = []
    for i in range(t):
        n, k = list(map(int, input().split()))
        nums = list(map(int, input().split()))
        res.append(zeroRemainderArray(nums, k))
    print(*res, sep="\n")
        
        
