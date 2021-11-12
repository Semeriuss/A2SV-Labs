from collections import Counter

def zeroRemainderArray(nums, k):
    requiredAdditions = []

    x = 1
    for num in nums:
        if num % k != 0:
            requiredAdditions.append(k - num%k)
        else:
            requiredAdditions.append(0)
    
    additionsMap = Counter(requiredAdditions)
    sortedSteps = sorted(additionsMap.items(), key=lambda x: (x[1], x[0]), reverse=True)

    maxSteps, maxAmount = 0, 0
    for amount, steps in sortedSteps:
        if amount != 0 and steps != 0:
            maxSteps = steps
            maxAmount = amount
            break
        
    # print(sortedSteps, maxSteps, maxAmount)
    if maxSteps == 0 or maxAmount == 0:
        return 0
    else:
        requiredSteps = 0
        for i in range(maxSteps):
            requiredSteps = max(((k*i) + maxAmount), requiredSteps)
        return requiredSteps + 1

    
        

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
        