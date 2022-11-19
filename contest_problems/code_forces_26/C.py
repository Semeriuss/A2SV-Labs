from itertools import accumulate
for _ in range(int(input())):
    n = int(input())
    red = list(map(int, input().split()))
    m1 = total = 0
    for num in red:
        total += num
        m1 = max(m1, total)

    
    m = int(input())
    blue = list(map(int, input().split()))
    m2 = total = 0
    for num in blue:
        total += num
        m2 = max(total, m2)
    
    print(m1 + m2)