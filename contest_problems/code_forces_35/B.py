for _ in range(int(input())):
    n = int(input())
    ep = list(input())
    gp = list(input())

    count = 0
    for i in range(n):
        e, g = ep[i], gp[i]
        if g == '1':
            if e == '0':
                count += 1
            elif i - 1 >= 0 and ep[i - 1] == '1':
                ep[i - 1] = 'x'
                count += 1
            elif i + 1 < n and ep[i + 1] == '1':
                ep[i + 1] = 'x'
                count += 1

    print(count)
            