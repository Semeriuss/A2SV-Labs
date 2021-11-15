def saveMoreMice(n, mice):
    mice.sort()
    count = 0
    cost = n
    for i in range(len(mice) - 1, -1, -1):
        if cost < 0:
            break
        cost -= (n - mice[i])
        if cost > 0:
            count += 1
    return count

if __name__ == "__main__":
    t = int(input())
    res = []
    for i in range(t):
        n, k = list(map(int, input().split()))
        mice = list(map(int, input().split()))
        res.append(saveMoreMice(n, mice))
    print(*res, sep="\n")

