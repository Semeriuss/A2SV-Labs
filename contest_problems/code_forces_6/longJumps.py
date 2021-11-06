
testcases = int(input())

tests = []

for i in range(testcases):
    n = int(input())
    jumps = list(map(int, input().split()))
    tests.append(jumps)

def findLongestJump(jumps): 
    memo = {}
    for start in range(len(jumps) - 1, -1, -1): 
        if start + 1 + jumps[start] in memo:
            memo[start + 1] = memo[start + 1 + jumps[start]] + jumps[start]
        else:
            memo[start + 1] = jumps[start]
    return max(memo.values())

for test in tests:
    print(findLongestJump(test))