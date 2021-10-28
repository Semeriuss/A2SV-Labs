import sys
from math import factorial

input = sys.stdin.readline
n, m, t = tuple(list(map(int, input().split())))

def findCombination(n, m, t):
    minBoysCombo = factorial(n)/(factorial(n-4) * factorial(4))
    minGirlsCombo = factorial(m)/(factorial(m-1)) 
    restCombo = (factorial(n+m-5))/factorial(t - 5) if t - 5 != 0 else 1
    
    return int(minGirlsCombo * minBoysCombo * restCombo)

print(findCombination(n, m, t))

