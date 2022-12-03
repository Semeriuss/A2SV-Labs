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
        chars[i] = 1 if s1[i] != s2[i] else 0

    
    res = ["-"] * n
    char_count = 0

    for index, common in chars.items():
        if char_count == n - t:
            break
        if common:
            res[index] = s1[index]
            char_count += 1
    
    if char_count != n - t:
        print(-1)
    else:
        set1, set2 = set(list(s1)), set(list(s2))
        common = set1.intersection(set2)
        set1.difference_update(common)
        set2.difference_update(common)

        alphabet = set([chr(ord('a') + i) for i in range(26)])

        alphabet.difference_update(set1)
        alphabet.difference_update(set2)
        if not alphabet:
            print(-1)
        placeHolder = alphabet.pop()
        for i in range(n):
            if res[i] == "-":
                res[i] = placeHolder
    

            
        print("".join(res))
