def solve(heights, requests):
    N = len(heights)
    required = []
    res = [0]
    mx = 0
    for i, height in enumerate(heights):
        mx = max(height, mx)
        required.append(mx)
        res.append(height + res[i])

    for request in requests:
        l, r = 0, N
        while l < r:
            mid = l + (r - l)//2 
            if required[mid] > request:
                r = mid
            else:
                l = mid + 1
        print(res[l], end = " ")
    print()
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        h = list(map(int, input().split()))
        r = list(map(int, input().split()))
        solve(h, r)