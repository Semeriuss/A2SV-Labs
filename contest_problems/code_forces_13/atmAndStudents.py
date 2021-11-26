def maxService(amount, line):
    maxServed = 0, 0
    cost = amount
    sp, ep = 0, 0

    while ep < len(line):
        print(maxServed, (sp, ep), cost, line[ep])
        if line[ep] >= 0:
            cost += line[ep]
            ep += 1
        else:
            if abs(line[ep]) > cost:
                maxServed = (sp, ep - 1) if (ep - sp) > (maxServed[1] - maxServed[0]) else maxServed
                sp = ep + 1
                cost = amount
            else:
                # maxServed = max(maxServed, (sp, ep))
                maxServed = (sp, ep - 1) if (ep - sp) > (maxServed[1] - maxServed[0]) else maxServed
                cost += line[ep]
        maxServed = (sp, ep - 1) if (ep - sp) >= (maxServed[1] - maxServed[0]) else maxServed
        ep += 1
    # print(maxServed[0], maxServed[1], sum(line[maxServed[0]: maxServed[1] + 1]) + cost)
    return (maxServed[0] + 1, maxServed[1] + 1) if sum(line[maxServed[0]: maxServed[1] + 1]) + cost >= 0 else -1

amount = 10
line = [-16, 2, -6, 8]

# amount = 1000
# line = [-100000, -100000, -100000]

amount = 0
line = [2, 6, -164, 1, -1, -6543]

amount = 1
line = [-1]
print(maxService(amount, line))
        