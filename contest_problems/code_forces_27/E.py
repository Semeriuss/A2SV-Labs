n = int(input())
cost = list(map(int, input().split()))
strings = []
strings_reversed = []
for i in range(n):
    strings.append(input())
    strings_reversed.append(strings[-1][::-1])

normal, reverse = [float("inf")] * n, [float('inf')] * n
normal[0] = 0
reverse[0] = cost[0]

for i in range(1, n):
    if strings[i] >= strings[i - 1]:
        normal[i] = normal[i - 1]
    if strings[i] >= strings_reversed[i - 1]:
        normal[i] = min(normal[i], reverse[i - 1])
    if strings_reversed[i] >= strings[i - 1]:
        reverse[i] = normal[i - 1] + cost[i]
    if strings_reversed[i] >= strings_reversed[i - 1]:
        reverse[i] = min(reverse[i], reverse[i - 1] + cost[i])

res = min(normal[-1], reverse[-1])
print(-1 if res == float('inf') else res)


