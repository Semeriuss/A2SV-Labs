import sys
from math import comb

t = int(input())

tests = []
for i in range(t):
    n, l, r = tuple(list(map(int, input().split())))
    a = list(map(int, input().split()))
    tests.append(((n,l,r), a))

def limitPairs(left, right, nums):
    
    nums.sort()
    n = len(nums)
    badones = 0
    lp, rp = 0, n-1
    while lp < rp:
        if nums[rp] + nums[lp] < left:
            badones += rp - lp    
            break    
        rp -= 1
    lp, rp = 0, n-1
    while lp < rp:
        if nums[rp] + nums[lp] > right:
            badones += rp - lp    
            break    
        lp += 1
    
    return comb(n, 2) - badones


for test in tests:
    
    (n,l,r), a = test
    print(limitPairs(l,r,a))


