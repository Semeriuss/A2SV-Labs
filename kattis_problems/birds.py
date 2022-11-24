l, d, n = map(int, input().split())

pos = []
for index in range(n):
    pos.append(int(input()))

pos.sort()
currPos = l - 6
res = 0
while pos:
    nextPos = pos.pop() 
    available = 1 + (currPos - nextPos - d)//d
    if available > 0:
        res += available
    currPos = nextPos - d

if currPos + d - 6 >= d:
    available = 1 + (currPos - 6)//d
    res += available
print(res)