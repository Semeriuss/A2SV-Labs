def longestOnes(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """

    endPointer = 0
    startPointer = 0
    zero_credit = k
    max_one_count = 0
    n = len(nums)

    # nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    # k = 3

    #s = 4    e = 5  loz = 5   zc =   moc = 5
    while endPointer < n:
        print(startPointer, endPointer, zero_credit)
        if nums[endPointer] != 1 and zero_credit < 1:
            max_one_count = max(endPointer - startPointer, max_one_count)
            if nums[startPointer] == 0:
                startPointer += 1
            else:
                while nums[startPointer] == 1:
                    startPointer += 1
                startPointer += 1
            zero_credit += 1 
            
        
        elif nums[endPointer] != 1:
            endPointer += 1
            zero_credit -= 1
        
        else:
            endPointer += 1
    max_one_count = max(endPointer - startPointer, max_one_count)
    
    return max_one_count
    
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1,0,0,1,1,1,0,1,1,0,1,0,1,0,0,0,1,0,1,1,1,1,1,0,1,1,0,0]
k = 3

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3

print(longestOnes(nums, k))