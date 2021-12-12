def permute(nums, i, res):
    if i == len(nums):
        res.append(nums)

    for j in range(i, len(nums)):
        perm = nums[:]
        perm[i], perm[j] = perm[j], perm[i]
        permute(perm, i + 1, res)

    return res

res = []
nums = [1,2,3]
nums = [1]
print(permute(nums, 0, res))