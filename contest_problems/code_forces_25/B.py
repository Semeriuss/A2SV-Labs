from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    counter = Counter(a)
    count = 0
    evens = 0
    for k, v in counter.items():
        if v % 2 != 0:
            count += 1
        else:
            evens += 1
    if evens:
        if evens % 2 == 0:
            count += evens 
        else:
            count += (evens - 1)
    print(count)