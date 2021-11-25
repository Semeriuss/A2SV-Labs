def teamComposition(a, b):   
    if a + b < 4:
        return 0

    return min(a, b, (a + b)//4)



if __name__ == "__main__":
    t = int(input())
    res = []
    for i in range(t):
        mathematician, programmer = map(int, input().split())
        res.append(teamComposition(mathematician, programmer))
    print(*res, sep="\n")        