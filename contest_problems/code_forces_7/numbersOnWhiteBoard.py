import math
t = int(input())

tests = []
for i in range(t):
    tests.append(int(input()))

def minNumberOnBoard(n):
    nums = [i for i in range(1, n + 1)]

    removedNums = []
    for i in range(n - 1):
        a = nums.pop()
        b = nums.pop()
        removedNums.append([b, a])
        nums.append(math.ceil((a + b)/2))
    
    
    minNum = nums[0]
    print(minNum)
    for nums in removedNums:
        print(nums[0], nums[1])
    
for test in tests:
    minNumberOnBoard(test)

    
    