def hemoseShopping(x, nums):

    sortedNums = sorted(nums)
    canBeSorted = "YES"
    for i in range(len(nums)):
        if nums[i] != sortedNums[i] and max(len(nums) - i - 1, i) < x:
            canBeSorted = "NO"          
    return canBeSorted

if __name__ == "__main__":
    t = int(input())
    res = []
    for i in range(t):
        n, x = map(int, input().split())
        nums = list(map(int, input().split()))
        res.append(hemoseShopping(x, nums))
    print(*res, sep="\n")
                    