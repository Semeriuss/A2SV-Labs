from functools import cache
n = int(input())
activities = list(map(int, input().split()))

@cache
def dfs(i, prev):
    if i == n:
        return 0
    a = activities[i]
    if a == 1 and prev != 'Contest':
        return dfs(i + 1, 'Contest')
    elif a == 2 and prev != 'Gym':
        return dfs(i + 1, 'Gym')
    elif a == 3:
        if prev == 'Gym':
            return dfs(i + 1, 'Contest')
        elif prev == 'Contest':
            return dfs(i + 1, 'Gym')
        else:
            return min(dfs(i + 1, 'Contest'), dfs(i + 1, 'Gym'))
    else:
        return 1 + dfs(i + 1, 'Rest')

print(dfs(0, 'Rest'))


