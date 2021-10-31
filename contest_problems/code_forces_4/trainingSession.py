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

    for topic, diff in problemSet:
        topics[topic] += 1
        difficulties[diff] += 1
    
    possibleWays = comb(len(problemSet), 3)
    
    for topic, difficulty in problemSet:
        repeatedOnes = (topics[topic] - 1) * (difficulties[difficulty] - 1)
        possibleWays -= repeatedOnes        
    
    return possibleWays

for test in tests:
    print(trainingSession(test))


