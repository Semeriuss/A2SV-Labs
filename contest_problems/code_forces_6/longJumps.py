import sys

sys.setrecursionlimit(300000)
testcases = int(input())

tests = []
for i in range(testcases):
    jumps2 = [0]
    n = int(input())
    jumps = list(map(int, input().split()))
    jumps2.extend(jumps)
    tests.append(jumps2)

def calculateJump(start, jumps, score, memo):

    if start >= len(jumps):
        return 0

    if memo[start]:
        return memo[start]

    
    memo[start] = jumps[start] + calculateJump(start + jumps[start], jumps, score, memo)
    return memo[start]



def findLongestJump(jumps): 
    maxJump = 0 
    memo = [0 for _ in range(len(jumps) + 1)] 
    
    for start in range(1, len(jumps)): 
        if memo[start] != 0:
            maxJump = max(maxJump, memo[start])
        else:
            maxJump = max(maxJump, calculateJump(start, jumps, 0, memo))

    return maxJump

for test in tests:
    print(findLongestJump(test))