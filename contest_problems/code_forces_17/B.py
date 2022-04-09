from collections import deque

def solve(num):
    if num%32768 == 0: return 0
    que = deque([(32768, 0)])
    mod = 32768
    while que:
        curr, steps = que.popleft()
        if curr%mod == 0:
            return steps
        if curr%2==0 and curr > 0: que.append(((curr//2)%mod, steps + 1))
        if curr > 0: que.append(((curr - 1)%mod, steps + 1))

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    res = []
    for num in nums:
        res.append(solve(num))
    print(*res)