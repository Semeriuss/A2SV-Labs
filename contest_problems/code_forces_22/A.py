def solve(s):
    N = len(s)
    if N % 2 != 0:
        return "NO"
    return "YES" if s[:N//2] == s[N//2:]  else "NO"

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        print(solve(s))