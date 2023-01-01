for _ in range(int(input())):
    s = list(input())
    curr_min = '9'
    for i in range(len(s) - 1, -1, -1):
        if s[i] <= curr_min: 
            curr_min = s[i]
        else:
            s[i] = str(min(int(s[i]) + 1, 9))
    s.sort()
    print("".join(s))
            