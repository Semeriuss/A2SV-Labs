t = int(input())

tests = []
for i in range(t):
    tests.append([int(char) for char in input()])

def ternaryString(nums):
    count = [0, 0, 0]

    ep = 0
    sp = 0

    def checkCount(count):
        return min(count) != 0
    
    minLength = float("inf") 
    count[nums[0] - 1] += 1
    while sp < len(nums) - 1 and ep < len(nums):
        if checkCount(count):
            minLength = min(minLength, ep - sp + 1)
            count[nums[sp] - 1] -= 1
            sp += 1
        
        else:
            ep += 1
            if ep < len(nums):
                count[nums[ep] - 1] += 1
    return minLength if minLength != float("inf") else 0
 

res = []
for test in tests:
    res.append(ternaryString(test))

print(*res, sep="\n")




















# 3
# 1
# 3
# 2
# 3
# 3...




# 3
# 3
# 3
# 3
# 3
# 3...