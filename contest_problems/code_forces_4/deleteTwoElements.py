import sys
from collections import defaultdict

input = sys.stdin.readline
testcases = int(input())

tests = []
for i in range(testcases):
    input = sys.stdin.readline
    n = int(input())

    input = sys.stdin.readline
    nums = list(map(int, input().split()))
    tests.append(nums)

def deleteTwoElements(nums):
    n = len(nums)
    summation = sum(nums)
    avg = summation/n
    wantedSum = 2 * avg
    
    hashset = set()

    ways = 0

    count = defaultdict(int)    

    for num in nums:
        if num in hashset:
            ways += count[wantedSum - num]
        hashset.add(wantedSum - num)
        count[num] += 1
    
    return ways

# tests = [[1, 2, 3, 4, 5, 6, 7], 
#         [50, 20, 10],
#         [1, 3, 4, 5, 7],
#         [8, 8, 8, 8],
#         [8, 8, 4, 4]]

for test in tests:
    print(deleteTwoElements(test))
