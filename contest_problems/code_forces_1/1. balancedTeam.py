import sys

input = sys.stdin.readline
n = int(input())

input = sys.stdin.readline
skills = list( map(int, input().split()))


    
def maxBalancedTeam(skills):
    maxTeamsList = []
    for i in range(len(skills)-1):
        maxTeam = 1
        for j in range(i+1, len(skills)):
            if abs(skills[i] - skills[j]) <= 5:
                maxTeam += 1
        maxTeamsList.append(maxTeam)
    
    return max(maxTeamsList)

def maxBalancedTeam(skills):

    minRange = 0
    maxRange = 0

    for num in skills:
        if num - 5 > minRange:
            minRange = num
        if num + 5 > maxRange:
            maxRange = num
    
    maxTeams = 0

    for num in skills:
        if minRange <= num <= maxRange:
            maxTeams += 1
    
    return maxTeams

def maxBalancedTeam(skills):

    skills.sort()

    n = len(skills)
    startPointer, endPointer, maxTeams = 0, 0, 0

    while endPointer < n:
        if skills[endPointer] - skills[startPointer] > 5:
            startPointer += 1
        else:
            endPointer += 1
            maxTeams = max(endPointer - startPointer, maxTeams)
    
    return maxTeams
            



print(maxBalancedTeam(skills))


