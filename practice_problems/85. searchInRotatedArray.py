from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minIndex = self.findMinIndex(nums)
        start = minIndex if target <= nums[len(nums) - 1] else 0
        end = minIndex if target > nums[len(nums) - 1] else len(nums) - 1
        print(minIndex, start, end)
        while start <= end:
            mid = start + (end - start)//2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid
        return -1
        
    def findMinIndex(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return left

nums = [4,5,6,7,0,1,2]
target = 0

nums = [4,5,6,7,0,1,2]
target = 3

nums = [1]
target = 0

nums = [1,2,4,5,6,7,8,9]
target = 3

nums = [19,21,24,25,26,27,67,88,111,1111,3242,10000,-10000,-3434,-454,-45,-5,-2,0,1,2,4,5,6,7,8,9]
target = 111

nums = [2,3,-5,-4,-3,-2,-1,0,1]
target = 2

nums = [19,21,24,25,26,27,67,88,111,1111,3242,10000,-10000,-3434,-454,-45,-5,-2,0,1,2,4,5,6,7,8,9]
target = 21

nums = [1,3]
target = 3

nums = [8,9,2,3,4]
target = 9
print(Solution().search(nums, target))        