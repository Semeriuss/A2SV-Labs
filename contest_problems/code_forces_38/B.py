for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    evens = sum(1 for x in a if x % 2 == 0)
    odds = n - evens
    if abs(odds - evens) > 1:
        print(-1)
    elif n % 2 == 1:
        if odds > evens:
            print(-1)
        else:
            count = 0
            for i, num in enumerate(a):
                if a[i] % 2 != i % 2:
                    count += 1
            print(count//2)
    else:
        if odds != evens:
            print(-1)
        else:
            count = 0
            for i, num in enumerate(a):
                if a[i] % 2 != i % 2:
                    count += 1
            print(count//2)
