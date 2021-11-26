def maxService(amount, line):
    maxServed = 0, 0
    cost = amount
    sp, ep = 0, 0

    while ep < len(line) and sp <= ep:
        if line[ep] >= 0:
            cost += line[ep]
            maxServed = maxServed if maxServed[1] - maxServed[0] > ep - sp else (sp + 1, ep + 1)
            ep += 1
        
        else:
            if abs(line[ep]) > cost:
                maxServed = maxServed if maxServed[1] - maxServed[0] >= ep - sp - 1 else (sp + 1, ep)
                if line[sp] >= 0:
                    cost -= line[sp] 
                else:
                    cost += line[sp] * -1
                    sp += 1
            else:
                cost += line[ep]
                maxServed = maxServed if maxServed[1] - maxServed[0] > ep - sp else (sp + 1, ep + 1)
                ep += 1
        # print(line[ep], cost)
    return f'{maxServed[0]} {maxServed[1]}' if maxServed != (0, 0) else -1

if __name__ == "__main__":
    t = int(input())
    res = []
    for i in range(t):
        n, s = map(int, input().split())
        line = list(map(int, input().split()))
        res.append(maxService(s, line))
    print(*res, sep="\n")

# 1
# 9 17
# 8 -14 -7 -3 -3 3 10 -16 -5