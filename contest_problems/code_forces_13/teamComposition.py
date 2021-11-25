def teamComposition(mathematician, programmer):
    a, b = (mathematician, programmer) if mathematician <= programmer else (programmer, mathematician)
    count = 0
    while a > 0 and b > 2:
        a -= 1
        b -= 3
        a, b = (a, b) if a <= b else (b, a)
        if a >= 0 and b >= 0:
            count += 1
    
    return count

def teamComposition(mathematician, programmer, memo):
    a, b = (mathematician, programmer) if mathematician <= programmer else (programmer, mathematician)
    if (a, b) in memo:
        return memo[(a,b)]
    if a <= 0 or b <= 0:
        return 0

    if a > 0 and b > 2:
        memo[(a,b)] = 1 + teamComposition(a - 1, b - 3, memo)
        return memo[(a,b)]
    return 0



if __name__ == "__main__":
    t = int(input())
    res = []
    for i in range(t):
        mathematician, programmer = map(int, input().split())
        res.append(teamComposition(mathematician, programmer, {}))
    print(*res, sep="\n")        