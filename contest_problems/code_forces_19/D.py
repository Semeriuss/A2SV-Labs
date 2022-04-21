def solve(s : str):
    wc, bc, rc = s.count('W'), s.count('B'), s.count('R')
    if bc == 0 and rc > 0 or rc == 0 and bc > 0:
        return "NO"
    if s.startswith("BW") or s.startswith("RW"):
        return "NO"
    if s.endswith("WB") or s.endswith("WR"):
        return "NO"
    if "WBW" in s or "WRW" in s:
        return "NO"
    if "BBBW" in s or "WBBB" in s or "RRRW" in s or "WRRR" in s:
        return "NO"
    return "YES"

if __name__ == "__main__":
    t = int(input())
    res = []
    for _ in range(t):
        n = int(input())
        res.append(solve(input()))
    print(*res)