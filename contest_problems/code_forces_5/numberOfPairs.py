import sys

t = int(input())

tests = []
for i in range(t):
    n, l, r = tuple(list(map(int, input().split())))
    a = list(map(int, input().split()))
    tests.append(((n,l,r), a))

def limitPairs(left, right, nums):
    possiblePair = set()
    count = 0
    for num in nums:
        if num in possiblePair:
            count += 1

        if left - num > 0:
            possibles = left - num
            while left + possibles <= right:
                possiblePair.add(possibles)
                possibles += 1
            
        if right - num > 0:
            possibles = right - num
            while right + possibles >= left:
                possiblePair.add(possibles)
                possibles -= 1    
    return count


for test in tests:
    
    (n,l,r), a = test
    print(limitPairs(l,r,a))


