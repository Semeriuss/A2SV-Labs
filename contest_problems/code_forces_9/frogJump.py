def frogJump(s):
    
    sp = 0
    ep = 0

    longestJump = 0
    currJump = 0
    while ep < len(s):
        if s[ep] == 'L':
            currJump += 1
        else:
            sp = ep
            currJump = 0
        ep += 1
        longestJump = max(longestJump, currJump)
    
    return longestJump + 1

if __name__ == '__main__':
    t = int(input())
    res = []
    for i in range(t):
        res.append(frogJump(input()))
    print(*res, sep="\n")

