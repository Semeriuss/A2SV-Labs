def solve(nums):
    n = len(nums)
    if n == 1 or len(set(nums)) == 1:
        return 1
    j = 0
    res = 0
    thickness = 1
    while j < n:
        thickness += 1
        presum = sum(nums[0 : thickness])
        currsum = 0
        currThickness = 0
        for i in range(thickness, len(nums)):
            currsum += nums[i]
            currThickness += 1
            if currsum == presum:
                currsum = 0
                res = max(res, thickness, currThickness)
                currThickness = 1
            elif currsum > presum:
                break
        else:
            return res if res != 0 else n
        j += 1
            
    return n

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        print(solve(nums))