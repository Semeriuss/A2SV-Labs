t = int(input())

tests = []
for i in range(t):
    tests.append([int(char) for char in input()])

def ternaryString(nums):
    nummap = {1: 0, 2: 0, 3: 0}

    ep = 0
    sp = 0

    def allIn(nummap):
        return nummap[1] != 0 and nummap[2] != 0 and nummap[3] != 0
    
    minLength = float("inf") 
    nummap[nums[0]] += 1
    while sp < len(nums) - 1 and ep < len(nums):
        if allIn(nummap):
            minLength = min(minLength, ep - sp + 1)
            nummap[nums[sp]] -= 1
            sp += 1
        
        else:
            ep += 1
            if ep < len(nums):
                nummap[nums[ep]] += 1
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