def smallestMirror(s):
    if len(s) == 1: return ""
    res = s[0]
    for i in range(1, len(s)):
        if ord(s[i]) < ord(s[i - 1]):
            res += s[i]
        else:
            break
    return res + res[::-1]

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        print(smallestMirror(s))

