def divisibleSumPairs(n, k, ar):
    ar.sort()
    rem = [[] for _ in range(k)]
    
    for num in ar:
        rem[num % k].append(num)
    
    print(rem)
    count = 0
    for i in range(len(rem[0]) - 1):
        for j in range(i + 1, len(rem[0])):
            if rem[0][i] != rem[0][j]:
                count += 1
            else:
                count += 2
            
    for i in range(1, k//2 + 1):
        if i == k - i:
            if not rem[i]: continue
            for j in range(len(rem[i]) - 1):
                for m in range(j + 1, len(rem[i])):
                    if rem[i][j] != rem[i][m]:
                        count += 1
                    else:
                        count += 2
        else:
            mod1 = rem[i]
            mod2 = rem[k - i]
            if not mod1 or not mod2: continue
            for i in range(len(mod1)):
                for j in range(len(mod2)):
                    if mod1[i] != mod2[j]:
                        count += 1
                    else:
                        count += 2

    return count

n, k = 5, 2
ar = [5, 9, 10, 7, 4]

n, k = 100, 40
ar = list(map(int , "13 91 5 100 5 12 5 79 99 87 59 65 62 73 93 73 63 65 59 46 67 35 22 55 50 53 38 79 75 44 95 53 5 73 44 94 95 21 60 2 32 48 72 13 91 74 79 99 17 31 53 20 88 17 54 47 56 79 23 49 95 81 9 50 12 20 45 82 44 82 93 15 73 51 65 96 4 77 37 41 30 11 65 100 62 51 64 48 12 11 68 81 46 37 10 46 75 82 21 23".split()))

print(divisibleSumPairs(n, k, ar))