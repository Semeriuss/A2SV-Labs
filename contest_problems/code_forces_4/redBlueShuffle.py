import sys
from math import perm


input = sys.stdin.readline
testCases = int(input())

tests = []
for i in range(testCases):
    input = sys.stdin.readline
    cardSize = int(input())

    input = sys.stdin.readline
    reds = list(input().rstrip())

    input = sys.stdin.readline
    blues = list(input().rstrip())

    tests.append((reds, blues))

def redBlueShuffle(reds, blues):
    redCount, blueCount = 0, 0
    for i in range(len(reds)):
        if reds[i] > blues[i]:
            redCount += 1
        elif reds[i] < blues[i]:
            blueCount += 1
        else:
            redCount += 1
            blueCount += 1


    if blueCount > redCount:
        return 'BLUE'
    elif redCount > blueCount:
        return 'RED'
    else:
        return 'EQUAL'

for test in tests:
    reds, blues = test
    print(redBlueShuffle(reds, blues))
    