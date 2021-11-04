import sys
from collections import defaultdict

sys.setrecursionlimit(90100)

input = sys.stdin.readline
n, target = tuple(list(map(int, input().split())))

input = sys.stdin.readline
portals = list(map(int, input().split()))

def pathExists(n, target, portals):
    
    start = 0
    while start < n - 1:
        start += portals[start]
        if start + 1 == target:
            return "YES"
        if start + 1 > target:
            return "NO"
    return "NO"

print(pathExists(n, target, portals))


