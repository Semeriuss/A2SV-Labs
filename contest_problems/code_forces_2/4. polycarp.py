import sys

input = sys.stdin.readline
n = int(input())

tests = []
for i in range(n):
    input = sys.stdin.readline
    tests.append(input())

def polycarp(string):
    pos = 0
    last_char = ""
    count = 0 
    
    while pos < len(string):        
        if string[pos] == 'w':
            count += 1    
        elif string[pos] == 'v' and last_char == 'v':
            count += 1

        last_char = string[pos] if last_char != 'v' else ""
        pos += 1
        
    return count

# tests = ['vv', 'v', 'w', 'vwv', 'vwvvwv', 'vvwwvw', 'wvvvv']
# tests = ['wvvv']
for test in tests:
    print(polycarp(test))
