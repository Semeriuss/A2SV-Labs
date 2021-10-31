from collections import defaultdict
import sys
from math import comb

input = sys.stdin.readline
testcases = int(input())


tests = []
for i in range(testcases):
    input = sys.stdin.readline
    n = int(input())
    problemset = []
    for j in range(n):
        input = sys.stdin.readline
        problemset.append(tuple(list(map(int, input().split()))))
    tests.append(problemset)

def trainingSession(problemSet):
    topics, difficulties = defaultdict(int), defaultdict(int)

    for topic, difficulty in problemSet:
        topics[topic] += 1
        difficulties[difficulty] += 1
    
    repeatedOnes = 1
    repeats = False
    for count in topics.values():
        if count > 1:
            repeats = True
            repeatedOnes *= (count - 1)

    for count in difficulties.values():
        if count > 1:
            repeats = True
            repeatedOnes *= (count - 1)

        
    possibleWays = comb(len(problemSet), 3) - repeatedOnes if repeats else comb(len(problemSet), 3)
    return possibleWays

for test in tests:
    print(trainingSession(test))


