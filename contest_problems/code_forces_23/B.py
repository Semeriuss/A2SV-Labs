import bisect
def solve(heights, requests):
    N = len(heights)
    required = []
    mx = 0
    res = [0]
    for i, height in enumerate(heights):
        mx = max(height, mx)
        required.append(mx)
        res.append(height + res[i])

    ret = []
    for request in requests:
        index = bisect.bisect_right(required, request)
        ret.append(res[index])
    print(*ret)
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        h = list(map(int, input().split()))
        r = list(map(int, input().split()))
        solve(h, r)