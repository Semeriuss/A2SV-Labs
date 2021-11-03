import sys
from collections import defaultdict

input = sys.stdin.readline
n, target = tuple(list(map(int, input().split())))

input = sys.stdin.readline
portals = list(map(int, input().split()))

def pathExists(target, portals):
    transportaionMap = defaultdict(list)

    for i, cell in enumerate(portals):
        transportaionMap[cell].append((i + 1) + cell)
        if cell == 1 and (i + 1 + cell) == target:
            return "YES"
    return "No"
    
    # for cell in transportaionMap[1]:
    #     if cell == target:
    #         return "Yes"
    # return "No"

print(pathExists(target, portals))
