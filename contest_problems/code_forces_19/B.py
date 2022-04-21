from collections import Counter
def solve(nums):
    numset = Counter(nums)
    for num in numset:
        if numset[num] >= 3:
            return num
    return -1
    

if __name__ == "__main__":
    t = int(input())
    res = []
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        res.append(solve(nums))
    print(*res)