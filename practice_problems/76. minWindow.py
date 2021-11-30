from collections import Counter, defaultdict

def minWindow(s: str, t: str) -> str:
    t_letterCount = Counter(t)
    s_letterCount = {char : 0 for char in t_letterCount}

    substringExists = False
    sp, ep = 0, 0

    min_sp, min_ep = 0, len(s)

    def checkCount(sMap, tMap):
        for k, v in tMap.items():
            if sMap[k] < v:
                return False
        return True

    while ep < len(s):   
        # print(t_letterCount, s_letterCount)
        # print(sp, ep, s[min_sp:min_ep+1])
        if checkCount(s_letterCount, t_letterCount):
            substringExists = True
            print("answers", s[sp : ep + 1], ep - sp, min_ep - min_sp)
            min_sp, min_ep = (sp, ep) if (ep - sp) <= (min_ep - min_sp) else (min_sp, min_ep)

            if s[sp] in s_letterCount:
                s_letterCount[s[sp]] -= 1

            sp += 1
            print(t_letterCount, s_letterCount)
        else:
            if s[ep] in s_letterCount:
                s_letterCount[s[ep]] += 1
            ep += 1

    while sp < len(s):
        if s[sp] in s_letterCount:
            s_letterCount[s[sp]] -= 1

        sp += 1
        # print(t_letterCount, s_letterCount)
        # print(min_sp, min_ep, s[min_sp:min_ep+1])
        if checkCount(s_letterCount, t_letterCount):
            min_sp = sp


    return s[min_sp:min_ep + 1] if substringExists else "j"


s = "ADOBECODEBANC"
t = "ABC"

# s = "a"
# t = "a"

# s = "a"
# t = "aa"

s = "ADOBECODEBANC"
t = "ABCBOE"
print(minWindow(s, t))

