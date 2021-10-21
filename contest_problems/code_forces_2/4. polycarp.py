import sys

input = sys.stdin.readline
n = int(input())

tests = []
for i in range(n):
    input = sys.stdin.readline
    tests.append(input())

def polycarp(string):
    r = False
    last_char = string[0]
    count = 0 if last_char == 'v' else 1
    for i in range(1, len(string)):
        
        if string[i] == 'w':
            count += 1
        elif string[i] == 'v' and last_char == 'v' and r == False:
            count += 1
            r = True
        elif r == True:
            r = False
        last_char = string[i]
    
        

    return count

# tests = ['vv', 'v', 'w', 'vwv', 'vwvvwv', 'vvwwvw', 'wvvvv']
for test in tests:
    print(polycarp(test))
