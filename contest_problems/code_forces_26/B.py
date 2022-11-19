from bisect import bisect_left
for _ in range(int(input())):
    n = int(input())
    if n % 7 == 0:
        print(n)
    else:
        multiples = set([7])
        i = 2
        while 7*i < 1000:
            multiples.add(7 * i)
            i += 1
        s = str(n)
        res = n
        FOUND = False
        for i, c in enumerate(s):
            if i == 0:
                for num in range(1, 9):
                    possible = int(str(num) + s[i + 1:])
                    if possible in multiples:
                        res = possible
                        FOUND = True
                        break
                if FOUND:
                    break
            else:
                for num in range(9):
                    possible = int(str(num) + s[i + 1:])
                    if possible in multiples:
                        res = possible
                        FOUND = True
                        break
                if FOUND:
                    break

        print(res)