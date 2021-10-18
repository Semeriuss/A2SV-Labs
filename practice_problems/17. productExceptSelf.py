def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rty
    """

    def mul(array):
        result = 1
        for i in array:
            result *= i

        return result
            

    productList = []
    for i in range(n:=len(nums)):
        if i == 0:
            productList.append(mul(nums[i+1:]))
        elif i == n-1:
            productList.append(mul(nums[:n-1]))
        else:
            productList.append(mul(nums[:i] + nums[i+1:]))

    return productList
#O(n) time and space     
def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rty
    """
    answer = [0 for _ in range(len(nums))]
    hasZero = False
    zeroCount = 0
    result = 1
    
    for i in nums:
        if i != 0:
            result *= i
        else:
            hasZero = True
            zeroCount += 1
            
    if zeroCount > 1:
        return answer
    
    for i in range(len(nums)):
        if hasZero and nums[i] != 0:
            answer[i] = 0
        elif nums[i] != 0:
            answer[i] = result // nums[i]
        else:
            answer[i] = result
    return answer

#O(n) time, O(1) space 
def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rty
    """
    zeroCount = 0
    result = 1
    
    for i in nums:
        if i != 0:
            result *= i
        else:
            zeroCount += 1
            
    if zeroCount > 1:
        return [0 for _ in range(len(nums))]
    
    for i in range(len(nums)):
        if zeroCount > 0 and nums[i] != 0:
            nums[i] = 0
        elif nums[i] != 0:
            nums[i] = result // nums[i]
        else:
            nums[i] = result
    return nums

# clean code

def countZeros(nums):
    count = 0
    for i in nums:
        if i == 0:
            count += 1
    return count

def multiplyWithoutZero(nums):
    result = 1
    for i in nums:
        if i != 0:
            result *= i
    return result

def productWithoutSelf(nums, productWithoutZero, zeroCount):
    if zeroCount > 1:
        return [0 for _ in range(len(nums))]
    for i in range(len(nums)):
        if zeroCount > 0 and nums[i] != 0:
            nums[i] = 0
        elif nums[i] != 0:
            nums[i] = productWithoutZero // nums[i]
        else:
            nums[i] = productWithoutZero
    return nums
        

def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rty
    """

    zeroCount = countZeros(nums)
    productWithoutZero = multiplyWithoutZero(nums)
    return productWithoutSelf(nums, productWithoutZero, zeroCount)

    


tests = [[1,2,3,4], [-1,1,0,-3,3], [2,3,0,4,0]]
for test in tests:
    print(productExceptSelf(test))

        
