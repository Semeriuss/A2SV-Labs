b = int(input())
bskills = sorted(map(int, input().split()))
g = int(input())
gskills = sorted(map(int, input().split()))

i = j = pairs = 0
while i < b and j < g:
    if abs(bskills[i] - gskills[j]) <= 1:
        pairs += 1
        i += 1
        j += 1
    elif bskills[i] > gskills[j]:
        j += 1
    else:
        i += 1

print(pairs)

