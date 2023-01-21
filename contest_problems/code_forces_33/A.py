for _ in range(int(input())):
    n = int(input())
    print(max(0, ((n - 9) - (n - 9) % 3)//3 + 1))
