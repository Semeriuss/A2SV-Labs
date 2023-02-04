n = int(input())
resting_days = 0
prev = 'Rest'
activities = list(map(int, input().split()))

for i, a in enumerate(activities):
    if a == 1 and prev != 'Contest':
        prev = 'Contest'
    elif a == 2 and prev != 'Gym':
        prev = 'Gym'
    elif a == 3:
        if prev == 'Gym':
            prev = 'Contest'
        elif prev == 'Contest':
            prev = 'Gym'
        else:
            if i < n and activities[i + 1] == 1:
                prev = 'Gym'
            elif i < n and activities[i + 1] == 2:
                prev = 'Contest'
            elif i < n and activities[i + 1] == 3:
                prev = 'Contest'
            elif i < n and activities[i + 1] == 0:
                prev = 'Gym'
    else:
        resting_days += 1
        prev = 'Rest'
print(resting_days)


