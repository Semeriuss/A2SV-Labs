def wrongAdd(a, s):
    N = len(s)
    n = len(a)
    a = '0'*(N-n) + a
    s = s
    ap = N - 1 
    sp = N - 1
    ep = N - 1
    res = []
    while ap >= 0 and sp >= 0 and ep >= 0:
        print(int(a[ap]), int(s[sp: ep + 1]))
        if int(a[ap]) > int(s[sp: ep + 1]):
            if sp == 0: return -1
            if int(s[sp: ep + 1]) - int(a[ap]) > 9 or int(s[sp: ep + 1]) - int(a[ap]) < 0: return -1
            sp -= 1
        else:
            diff = abs(int(s[sp: ep + 1]) - int(a[ap]))
            res.append(str(diff))
            ap -= 1
            sp -= 1
            ep = sp
    
    if ap >= 0  and a[ap] != '0': return -1
    print(a, ap, s, sp, ep)
    return "".join(res[::-1]).lstrip('0')

if __name__ == "__main__":
    t = int(input())
    res = []
    for _ in range(t):
        a, s = input().split()
        res.append(wrongAdd(a, s))
    print(*res)
# print(wrongAdd("17236", "1106911"))
            