#O(n) time and space
def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    if len(nums) == 1: return nums[0]

    num_dict = {num : 0 for num in nums}
    for i in nums:
        num_dict[i] += 1

    for k, v in num_dict.items():
        if v == 1:
            return k

#O(n) time, O(1) space
def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    nums_sum = sum(nums)
    set_sum = sum(set(nums))
    return 2*set_sum - nums_sum
            
    
        
            
tests = [[2,2,1], [4,1,2,1,2], [1], [4,1,2,3,1,2,4]]
for test in tests:
    print(singleNumber(test))
                
                
                
