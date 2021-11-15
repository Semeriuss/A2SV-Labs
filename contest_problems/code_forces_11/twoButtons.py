def twoButtons(n, m):
   
    steps = 0
    while m > n:
        if m % 2 != 0:
            m += 1
        else:
            m //= 2
        steps += 1
            
    return steps + abs(n - m)
if __name__ == "__main__":
    n, m = map(int, input().split())
    if m > n:
        print(twoButtons(n, m))
    else:
        print(n - m)