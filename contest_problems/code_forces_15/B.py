def smallestMirror(s):
    res = s[0]
    for i in range(1, len(s)):
        if ord(s[i]) < ord(s[i - 1]):
            res += s[i]
        elif ord(s[i]) == ord(s[i - 1]) and s[0] != s[i]:
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

