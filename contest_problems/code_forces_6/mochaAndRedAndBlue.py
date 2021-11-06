import sys

input = sys.stdin.readline
testcases = int(input())

tests = []
for i in range(testcases):
    n = int(input())
    squares = input().rstrip()
    tests.append((n, squares))

def findMinImperfectnessHelper(squares, n, nextChar):
    if n >= len(squares):
        return 
    
    if n < 0:
        findMinImperfectnessHelper(squares, n + 1, nextChar)
    
    if squares[n] == '?' and not nextChar:
        findMinImperfectnessHelper(squares, n + 1, nextChar)

    if squares[n] == '?' and nextChar:
        squares[n] = nextChar
        nextChar = 'B' if nextChar == 'B' else 'R'
        findMinImperfectnessHelper(squares, n - 1, nextChar)
        findMinImperfectnessHelper(squares, n + 1, nextChar)
    
    if squares[n] == 'B':
        nextChar = 'R'
        findMinImperfectnessHelper(squares, n - 1, nextChar)
        findMinImperfectnessHelper(squares, n + 1, nextChar)
    
    if squares[n] == 'R':
        nextChar = 'B'
        findMinImperfectnessHelper(squares, n - 1, nextChar)
        findMinImperfectnessHelper(squares, n + 1, nextChar)



def findMinImperfectness(squares, n):
    tobeModified = list(squares)
    findMinImperfectnessHelper(tobeModified, 0, None)
    return "".join(tobeModified)

print(findMinImperfectness(squares, n))