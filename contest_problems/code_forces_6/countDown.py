import sys

input = sys.stdin.readline
testcases = int(input())

tests = []
for i in range(testcases):
    n = int(input())
    digits = input().rstrip()
    tests.append((n, digits))

def countDown(digits, n, memo):
    if n < 0:
        return 0

    if n in memo:
        return memo[n]

    if n >= len(digits):
        memo[n] = countDown(digits, n - 1, memo)
        return memo[n]

    if int(digits[n]) == 0:
        memo[n] = countDown(digits, n - 1, memo)
        return memo[n]
    
    elif int(digits[n]) != 0 and n == len(digits) - 1:
        memo[n] = int(digits[n]) + countDown(digits, n - 1, memo)
        return memo[n]

    else:
        memo[n] = 1 + int(digits[n]) + countDown(digits, n - 1, memo)
        return memo[n]
        


for test in tests:
    n, digits = test
    print(countDown(digits, n, {}))
        

