def solve(nums):
    org1, org2 = nums[0] % 2, nums[1] % 2
    for i in range(0, len(nums), 2):
        if nums[i] % 2 != org1:
            return "NO"
    
    for i in range(1, len(nums), 2):
        if nums[i] % 2 != org2:
            return "NO"
    
    return "YES"

if __name__ == "__main__":
    t = int(input())
    res = []
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        res.append(solve(nums))
    print(*res)