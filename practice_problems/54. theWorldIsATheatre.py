import sys
from math import factorial, comb
from itertools import combinations

input = sys.stdin.readline
n, m, t = tuple(list(map(int, input().split())))

def findCombination2(n, m, t):
    possiblities = 0

    for i in range(4, t):
        possiblities += comb(n, i) * comb(m,  t-i)

    print(possiblities)

def findCombination(n, m, t):

    def getComb(chosen_boys, chosen_girls):
        nonlocal n, m
        return comb(n, chosen_boys) * comb(m, chosen_girls)

    combos = []

    minBoysCombo = 4
    minGirlsCombo = t - minBoysCombo
    print(minBoysCombo, minGirlsCombo)
    ways = 0
    while 0 < minGirlsCombo and 3 < minBoysCombo:
        combos.append([minBoysCombo, minGirlsCombo])
        minBoysCombo += 1
        minGirlsCombo -= 1

    print(combos)
    for combo in combos:
        ways += getComb(combo[0], combo[1])
    
    return ways

print(findCombination(n, m, t))
findCombination2(n, m, t)