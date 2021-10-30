import sys
import collections
from math import factorial, perm


input = sys.stdin.readline
testCases = int(input())

tests = []
for i in range(testCases):
    input = sys.stdin.readline
    cardSize = int(input())

    input = sys.stdin.readline
    reds = list((input()))

    input = sys.stdin.readline
    blues = list((input()))

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

    # redDuplicates, blueDuplicates = collections.Counter(reds), collections.Counter(blues)
    # maxRedRepetition = max(redDuplicates.values())
    # maxBlueRepetition = max(blueDuplicates.values())
    # k = 0 if min(maxRedRepetition, maxBlueRepetition) == 1 else min(maxRedRepetition, maxBlueRepetition)

    toBePermuted = reds if len(set(reds)) > len(set(blues)) else blues
    possiblePermutations = perm(len(toBePermuted))
    blueWins = blueCount/(redCount + blueCount) * possiblePermutations
    redWins = redCount/(redCount + blueCount) * possiblePermutations

    if blueWins > redWins:
        return 'BLUE'
    elif redWins > blueWins:
        return 'RED'
    else:
        return 'EQUAL'

for test in tests:
    reds, blues = test
    print(redBlueShuffle(reds, blues))
    