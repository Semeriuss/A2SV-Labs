import sys

input = sys.stdin.readline
testcases = int(input())

tests = []
for i in range(testcases):
    n = int(input())
    squares = input().rstrip()
    tests.append((n, squares))

def findMinImperfectnessHelper(squares, n, nextChar, memo):

    if n in memo:
        return memo[n]

    if n >= len(squares):
        memo[n] = nextChar if nextChar else 'B'
        return memo[n]

    if n < 0:
        memo[n] = nextChar
        return memo[n]

    if squares[n] == '?' and not nextChar:
        memo[n] = findMinImperfectnessHelper(squares, n + 1, nextChar, memo)
        squares[n] = memo[n]

    if squares[n] == '?' and nextChar:
        memo[n] = nextChar
        squares[n] = memo[n]
        nextChar = 'B' if nextChar == 'R' else 'B'
        findMinImperfectnessHelper(squares, n - 1, nextChar, memo)

    
    if squares[n] == 'B':
        nextChar = 'R'
        findMinImperfectnessHelper(squares, n + 1, nextChar, memo)
        return nextChar
    
    if squares[n] == 'R':
        nextChar = 'B'
        findMinImperfectnessHelper(squares, n + 1, nextChar, memo)
        return nextChar



def findMinImperfectness(squares, n):
    tobeModified = list(squares)
    findMinImperfectnessHelper(tobeModified, 0, None, {})
    
    return "".join(tobeModified)

for test in tests:
    n, squares = test
    print(findMinImperfectness(squares, n))