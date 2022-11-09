for _ in range(int(input())):
    n, k = map(int, input().split())
    nextNum = (n//k + int(n%k != 0))*k
    print(nextNum//n + int(nextNum%n != 0))
    