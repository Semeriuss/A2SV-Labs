from collections import defaultdict
def solve(a):
    cnt = defaultdict(int)
    pairs = 0
    for i, num in enumerate(a):
        pairs += cnt[num - i]
        cnt[num - i] += 1
    return pairs
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solve(arr))