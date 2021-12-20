def isSquareString(s):
    N = len(s)
    if N % 2 == 1: return "NO"
    return "YES" if s[:N//2] == s[N//2:] else "NO"

if __name__ == "__main__":
    t = int(input())
    res = []
    for i in range(t):
        res.append(isSquareString(input()))
    print(*res)