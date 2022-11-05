def solve(s):
    upper = lower = res = mem = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i].islower():
            lower += 1
        if s[i].isupper():
            upper += 1
            mem += 1
        elif mem:
            mem -= 1
            res += 1
    return min(res, upper, lower)

print(solve(input()))
