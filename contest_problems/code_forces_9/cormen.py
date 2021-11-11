
def cormen(nums, k):

    totalNeededWalks = 0
    if len(nums) == 1:
        additionalWalks = [nums[0] + k - nums[0]]
        totalNeededWalks = k - nums[0]
        # break here
    else:
        additionalWalks = [nums[0]]
        for i in range(1, len(nums)):
            totalNeededWalks += (k - additionalWalks[i - 1] - nums[i])
            additionalWalks.append((k - additionalWalks[i - 1]))


    print(totalNeededWalks)
    print(additionalWalks)

def cormen(nums, k):
    
    totalNeededWalks = 0
    additionalWalks = nums.copy()
    needsMoreWalks = False
    for i in range(1, len(nums)):
        walks = nums[i - 1] + nums[i]
        if walks < k:
            needsMoreWalks = True
            break
    
    if needsMoreWalks:
        if len(nums) == 1:
            additionalWalks = [nums[0] + k - nums[0]]
            totalNeededWalks = k - nums[0]
        
        else:
            additionalWalks = [nums[0]]
            for i in range(1, len(nums)):
                totalNeededWalks += (k - additionalWalks[i - 1] - nums[i])
                additionalWalks.append((k - additionalWalks[i - 1] - nums[i]))

            for j in range(1, len(nums)):
                additionalWalks[j] += nums[j]
    
            
    print(totalNeededWalks)
    print(*additionalWalks, sep=" ")



# nums = [2, 0, 1]
# k = 5
# cormen(nums, k)

if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    cormen(nums, k)