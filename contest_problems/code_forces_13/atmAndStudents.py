def maxService(amount, line):
    maxServed, ans = -1, ""
    cost = amount
    sp, ep = 0, 0

    while ep < len(line) and sp <= ep:
        if line[ep] >= 0:
            cost += line[ep]
            ep += 1
        else:
            if abs(line[ep]) > cost:
                a = sp + 1
                b = ep

                if b - a > maxServed:
                    ans = str(a) + ' ' + str(b)
                    maxServed = b - a
                cost -= line[sp]
                sp += 1
            else:
                cost += line[ep]
                ep += 1
    a = sp + 1
    b = ep

    if b - a > maxServed:
        ans = str(a) + ' ' + str(b)
        maxServed = b - a

    return ans if ans else -1

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

# 1
# 4 10
# -16 2 -6 8