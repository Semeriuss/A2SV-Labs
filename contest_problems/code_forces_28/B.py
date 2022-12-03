for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    even = len(list(filter(lambda x : x % 2 == 0, a)))
    odd = len(a) - even

    res = sum(a)
    for _ in range(q):
        i, xi = map(int, input().split())
        if i % 2 == xi % 2 == 0:
            res += (even * xi)
        elif i % 2 == xi % 2 == 1:
            res += (odd * xi)
            even += odd 
            odd = 0
        elif i % 2 == 1 and xi % 2 == 0:
            res += (odd * xi)
        else:
            res += (even * xi)
            odd += even 
            even = 0
        print(res)