import sys

input = sys.stdin.readline
testcases = int(input())

tests = []
for i in range(testcases):
    n = int(input())
    digits = input().rstrip()
    tests.append((n, digits))

def countDown(digits, n):
    if n < 0:
        return 0

    if n >= len(digits):
        return countDown(digits, n - 1)

    if int(digits[n]) == 0:
        return countDown(digits, n - 1)
    
    elif int(digits[n]) != 0 and n == len(digits) - 1:
        return int(digits[n]) + countDown(digits, n - 1)
        
    else:
        return 1 + int(digits[n]) + countDown(digits, n - 1)
        


for test in tests:
    n, digits = test
    print(countDown(digits, n))
        

