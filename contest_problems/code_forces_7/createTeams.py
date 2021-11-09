
def maxTeams(teams, k):
    teams.sort()
    teamCount = 0
    group = 0
    for i in range(len(teams) - 1, -1, -1):
        if teams[i] >= k:
            teamCount += 1
        else:
            group += 1
            if teams[i] * group >= k:
                teamCount += 1
                group = 0

    return teamCount

if __name__ == "__main__":
    t = int(input())

    res = []
    for i in range(t):
        n, k = list(map(int, input().split()))
        teams = list(map(int, input().split()))
        res.append(maxTeams(teams, k))

print(*res, sep="\n")