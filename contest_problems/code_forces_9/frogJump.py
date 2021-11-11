
def frogJump(s):
    
    firstR = -1
    lastR = -1

    for i in range(len(s)):
        if s[i] == 'R':
            firstR = i
            break
    
    for j in range(len(s) - 1, -1, -1):
        if s[j] == 'R':
            lastR = j + 1
            break
    
    # print(firstR, lastR)
    if firstR < 0 and lastR < 0:
        return len(s) + 1
    
    else:
        return max(firstR, lastR) + 1

def frogJump(s):
    
    longestJump = 0
    for i in s:
        if i == 'L':
            longestJump += 1
        else:
            longestJump = 0
        longestJump = max(longestJump, 1)
    
    return longestJump

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



# tests = ["LRLRRLL", "L", "LLR", "RRRR", "LLLLLL", "R"]
# for test in tests:
#     print(frogJump(test))

if __name__ == '__main__':
    t = int(input())
    res = []
    for i in range(t):
        res.append(frogJump(input()))
    print(*res, sep="\n")

