def minStartValue(nums):
    prefixSum = [nums[0]]
    for i in range(1, len(nums)):
        prefixSum.append(nums[i] + prefixSum[i - 1])
    minVal = min(prefixSum) if min(prefixSum) < 0 else 0
    return abs(minVal) + 1

def minStartValue(nums):
    prefixSum = 0
    minVal = nums[0]
    for i in range(len(nums)):
        prefixSum += nums[i]
        minVal = min(prefixSum, minVal)
    minVal = min(minVal, 0)
    return abs(minVal) + 1

tests = [([2,3,4], 1), ([-1, 2, -3, 4], 3)]
for test in tests:
    nums, expected = test
    actual = minStartValue(nums)
    print(actual == expected, actual, expected)
        
    
