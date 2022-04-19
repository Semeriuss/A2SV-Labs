def solve(n, m):
    a, b = n - 1, m - 1
    if a > 1 and b == 0 or b > 1 and a == 0:
        return -1
    count = 0
    while a > 0 and b > 0:
        a -= 1
        b -= 1
        count += 2
    if a > 0:
        if a % 2 == 0:
            count += (a * 2) 
        else:
            count += (a * 2) - 1
    elif b > 0:
        if a % 2 == 0:
            count += (b * 2)
        else:
            count += (b * 2) - 1
    
    return count


if __name__ == "__main__":
    t = int(input())
    res = []
    for _ in range(t):
        n, m = map(int, input().split())
        res.append(solve(n, m))
    print(*res)