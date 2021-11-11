"""
Given an array of integers nums containing n + 1 integers
where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums,
return this repeated number.

You must solve the problem without modifying the array nums
and uses only constant extra space.
"""

def findDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uniqueLength = len(set(nums))
        duplicateLength = len(nums)
        uniqueSum = sum(set(nums))
        duplicateSum = sum(nums)
        
        if uniqueLength == 1: return nums[0]
        return (duplicateSum - uniqueSum)//(duplicateLength - uniqueLength)

def findDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare
    
def findDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def numbersLessThanOrEqualTo(n, nums):
            count = 0
            for num in nums:
                if num <= n:
                    count += 1
            return count
        
        lower = 1
        upper = len(nums) - 1
        ans = -1
        while lower <= upper:
            mid = (lower + upper)//2
            count = numbersLessThanOrEqualTo(mid, nums)
            # print("mid:", mid, "count:", count)  
            if count <= mid:
                lower = mid + 1
            elif count > mid:
                ans = mid
                upper = mid - 1
        
        return ans

nums = [1, 2, 3, 7, 5, 6, 8, 8]
# nums = [1, 2, 3, 7, 5, 6, 7, 7]
# nums = [1, 2, 2, 3, 4, 6, 7, 8, 9]
# nums = [1, 3, 4, 2, 2]
# nums = [1,2,3,3,4]
print(findDuplicate(nums))

            
            
