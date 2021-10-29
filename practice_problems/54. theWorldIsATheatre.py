import sys
from math import factorial, comb
from itertools import combinations

input = sys.stdin.readline
n, m, t = tuple(list(map(int, input().split())))

def findCombination(n, m, t):


    def getComb(chosen_boys, chosen_girls):
        nonlocal n, m
        return comb(n, chosen_boys) * comb(m, chosen_girls)
        
    
    def getCombination(chosen_boys, chosen_girls):
        nonlocal n, m
        minBoysCombo = factorial(n)/(factorial(chosen_boys) * factorial(n - chosen_boys))
        minGirlsCombo = factorial(m)/(factorial(chosen_girls) * factorial(m - chosen_girls)) 
        return int(minGirlsCombo * minBoysCombo)

    combos = []

    minBoysCombo = 4
    minGirlsCombo = t - minBoysCombo

    ways = 0
    while 0 < minGirlsCombo <= m and 3 < minBoysCombo <= n:
        combos.append([minBoysCombo, minGirlsCombo])
        minBoysCombo += 1
        minGirlsCombo -= 1

    print(combos)
    for combo in combos:
        # ways += getCombination(combo[0], combo[1])
        ways += getComb(combo[0], combo[1])
    
    return ways

print(findCombination(n, m, t))