from collections import Counter
for _ in range(int(input())):
    s = list(map(int, list(input())))
    count = Counter(s)
    curr_min = 10
    for i in range(len(s) - 1, 0, -1):
        if s[i] > curr_min: continue
        if s[i] < s[i - 1]:
            temp = min(count[s[i] + 1],  10)
            if s[i] + 1 != 9: count[s[i] + 1] = 0 
            for j in range(min(9, s[i] + 1), 9):
                if j > curr_min:
                    break 
                if j == 8:
                    count[j + 1] += temp
                else:
                    t = count[j + 1]
                    count[j + 1] = temp  
                    temp = t
            curr_min = s[i] - 1
    res = []
    for i in range(0, 10):
        res.append(str(i)*count[i])
    
    print("".join(res))
            