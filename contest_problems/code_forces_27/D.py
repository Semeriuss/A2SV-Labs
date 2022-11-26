n = int(input())
res = list(input())

if n == 1:
    for i in range(len(res)):
        if res[i] == '?':
            res[i] = 'a'

else:
    for i in range(len(res)):
        if res[i] == '?':
            res[i] = '!'

    for _ in range(1, n - 1):
        s = input()
        for index, c in enumerate(s):
            if s[index] != '?':
                if s[index] == res[index]: 
                    continue
                if res[index] == '!':
                    res[index] = s[index]
                else:
                    res[index] = '?'
    
    s = input()
    for index, c in enumerate(s):
        if s[index] != '?':
            if s[index] == res[index]:
                continue
            if res[index] == '!':
                res[index] = s[index]
            else:
                res[index] = '?'

    for i in range(len(res)):
        if res[i] == '!':
            res[i] = 'a'

print("".join(res))
