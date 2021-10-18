#O(n) time, O(n^2) space
def buildArray(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        ans = []
        for num in nums:
            ans.append(nums[num])
        return ans
    
#O(n) time, O(1) space
def buildArray(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        #a = qb + r
        q = len(nums)
        
        for i, num in enumerate(nums):
            b = nums[num] % q
            r = num
            nums[i] = q*b + r
        for i in range(len(nums)):
            nums[i] = nums[i]//q
            
        return nums

tests = [([0,2,1,5,3,4],[0,1,2,4,5,3]), ([5,0,1,2,3,4],[4,5,0,1,2,3])]
for test in tests:
    nums, expected = test
    actual = buildArray(nums)
    print(actual == expected, actual, expected)
