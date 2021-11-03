import sys

t = int(input())

tests = []
for i in range(t):
    n, l, r = tuple(list(map(int, input().split())))
    a = list(map(int, input().split()))
    tests.append(((n,l,r), a))

def limitPairs(left, right, nums):
    possiblePair = set()
    count = 0
    maxVal, secondMaxVal = float("-inf"), float("-inf")
    maxInd = -1
    for i, num in enumerate(nums):
        if num > maxVal:
            maxVal = num
            maxInd = i
    if maxInd == 0:
        secondMaxVal = max(nums[1:])
    elif maxInd == len(nums) - 1:
        secondMaxVal = max(nums[:len(nums)-1])
    else:
        secondMaxVal = max(nums[:maxInd] + nums[maxInd+1:])
    
    if maxVal + secondMaxVal < left:
        return 0

    for num in nums:
        if num in possiblePair:
            count += 1

        if left - num > 0:
            possibles = left - num
            while left + possibles <= right:
                possiblePair.add(possibles)
                possibles += 1
            
        if right - num > 0:
            possibles = right - num
            while right + possibles >= left:
                possiblePair.add(possibles)
                possibles -= 1   
    print(possiblePair) 
    return count


for test in tests:
    print()
    (n,l,r), a = test
    print(limitPairs(l,r,a))
    print()



