def cormen(nums, k):
    
    totalNeededWalks = 0
    additionalWalks = [nums[0]]
    
    for i in range(1, len(nums)):
        if additionalWalks[i - 1] + nums[i] < k:
            additionalWalks.append(nums[i] + k - additionalWalks[i - 1] - nums[i])
            totalNeededWalks += (k - additionalWalks[i - 1] - nums[i])
        else:
            additionalWalks.append(nums[i])
    
            
    print(totalNeededWalks)
    print(*additionalWalks, sep=" ")



# nums = [2, 0, 1]
# k = 5
# cormen(nums, k)

if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    cormen(nums, k)