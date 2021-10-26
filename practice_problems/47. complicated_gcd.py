import sys

input = sys.stdin.readline
a, b = tuple(list(map(int, input().split())))

def complicatedGCD(a, b):
    if a != b:
        return 1
    else:
        return a

# tests = [(1, 2), 
#         (61803398874989484820458683436563811772030917980576, 61803398874989484820458683436563811772030917980576)]
# for test in tests:
#     a, b = test
#     print(complicatedGCD(a, b))

print(complicatedGCD(a, b))
