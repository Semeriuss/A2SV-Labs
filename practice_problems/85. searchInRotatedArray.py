from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        mid = -1
        while left <= right:
            mid = (left + (right - left)//2)
            print("mid", mid, "left", left, "right", right)
            if nums[mid] > nums[0]:
                if target == nums[left]:
                    mid = left
                    break
                elif target == nums[right]:
                    mid = right
                    break
                elif target == nums[len(nums) - 1]:
                    mid = len(nums) - 1
                    break
                elif target < nums[mid] and target < nums[0]:
                    left = mid + 1
                elif target < nums[mid] and target > nums[0]:
                    right = mid - 1
                elif target > nums[mid] and target > nums[0]:
                    left = mid + 1
                elif target > nums[mid] and target < nums[0]:
                    mid = -1
                    break
                else:
                    break
            
            elif nums[mid] < nums[0]:
                if target == nums[left]:
                    mid = left
                    break
                elif target == nums[right]:
                    mid = right
                    break
                elif target < nums[mid] and target < nums[0]:
                    right = mid - 1
                elif target < nums[mid] and target > nums[0]:
                    mid = -1
                    break
                elif target > nums[mid] and target > nums[0]:
                    right = mid - 1
                elif target > nums[mid] and target < nums[0]:
                    left = mid + 1
                else:
                    break
            
            else:
                if target == nums[left]:
                    mid = left
                    break
                elif target == nums[right]:
                    mid = right
                    break
                break
        
        return mid if nums[mid] == target else -1

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
print(Solution().search(nums, target))        