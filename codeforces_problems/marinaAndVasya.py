n, t = map(int, input().split())
s1 = input().strip()
s2 = input().strip()

if t > n:
    print(-1)

elif t == 0:
    if s1 != s2:
        print(-1)
    else:
        print(s1)
else:
    chars = {}
    for i in range(n):
        chars[i] = s1[i] if s1[i] == s2[i] else ""

    res = ["-"] * n
    same = n - t 

    set1, set2 = set(list(s1)), set(list(s2))
    common = set1.intersection(set2)
    set1.difference_update(common)
    set2.difference_update(common)

    alphabet = set([chr(ord('a') + i) for i in range(26)])

    if same == 0:
        res = [""]*n
        for i in range(n):
            res[i] = set(filter(lambda x : x != s1[i] and x != s2[i], alphabet)).pop()
        print("".join(res))
    else:
        for i, c in chars.items():
            if same == 0:
                break 
            elif c:
                res[i] = c 
                same -= 1
        
        if same == 0:
            if alphabet:
                char = alphabet.pop()
                for i, c in enumerate(res):
                    if c == '-':
                        res[i] = set(filter(lambda x : x != s1[i] and x != s2[i], alphabet)).pop()
                print("".join(res))
            else:
                print(-1)
        else:
            same1 = same2 = same
            for i, c in enumerate(res):
                if same1 == 0:
                    break 
                if c == '-':
                    res[i] = s1[i]
                    same1 -= 1
            if same1 > 0:
                print(-1)
            else:
                for i, c in enumerate(res):
                    if same2 == 0:
                        break 
                    if c == '-':
                        res[i] = s2[i]
                        same2 -= 1
                
                if same2 > 0:
                    print(-1)
                else:
                    for i in range(len(res)):
                        if res[i] == '-':
                            res[i] = res[i] = set(filter(lambda x : x != s1[i] and x != s2[i], alphabet)).pop()
                    print("".join(res))
        