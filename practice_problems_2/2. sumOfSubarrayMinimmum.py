from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr.append(0)
        stack = [-1]
        res = 0

        for i in range(len(arr)):
            while arr[i] < arr[stack[-1]]:
                idx = stack.pop()
                res += arr[idx] * (i - idx) * (idx - stack[-1])
            stack.append(i)
        return res

print(Solution().sumSubarrayMins([3,1,2,4]))