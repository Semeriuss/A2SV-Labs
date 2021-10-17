def containsNearbyDuplicate(nums, k):
    if len(set(nums)) == len(nums) or k == 0:
        return False

    nums_set = set()
    start = 0
    end = 0

    while end < len(nums):
        if end - start > k:
            nums_set.remove(nums[start])
            start += 1

        else:
            if nums[end] in nums_set:
                return True
            else:
                nums_set.add(nums[end])
                end += 1
    return False

tests = [([1,0,1,1], 1, True),
         ([1,2,3,1,2,3], 2, False),
         ([1,2,3,1], 3, True)
         ]

for test in tests:
    nums, k, expected = test
    actual = containsNearbyDuplicate(nums, k)
    print("Passed" if actual == expected else "Failed")
