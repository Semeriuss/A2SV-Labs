import heapq
for _ in range(int(input())):
    n = int(input())
    s = input()
    pre_array = []
    total = 0
    for i in range(n):
        if s[i] == 'L':
            pre_array.append(i)
            total += i
        else:
            pre_array.append(n - i - 1)
            total += n - i - 1

    res = []
    pre_array.sort()
    for val in pre_array:
        if n - val - 1 > val:
            total += n - val - 1 - val
        res.append(total)
    print(*res)
