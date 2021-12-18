from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        def reverseSubArray(i, subarr):
            return subarr[:i+1][::-1] + subarr[i+1:]

        def findDesiredIndex(arr, target):
            for i, num in enumerate(arr):
                if num == target:
                    return i
                
        n = len(arr)
        res = []
        curr_max = n
        last = n
        while curr_max > 1:
            desiredIndex = findDesiredIndex(arr, curr_max)
            res.append(desiredIndex + 1)
            arr = reverseSubArray(desiredIndex, arr)
            print("subrev", arr)
            curr_max -= 1
            last -= 1
            arr = reverseSubArray(last, arr)
            res.append(last + 1)
            print("fullrev", arr)
        print(arr)
        return res

lst = [3,1,2,4]
lst = [3,2,4,1]
print(Solution().pancakeSort(lst))