from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer, rightMax = [0]*len(temperatures), float("-inf")
        for i in range(len(temperatures) - 1, - 1, -1):
            if temperatures[i] > rightMax:
                rightMax = temperatures[i]
            else:
                days = 1
                while temperatures[i + days] <= temperatures[i]:
                    days += answer[i + days]
                answer[i] = days
        return answer
                     

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(Solution().dailyTemperatures(temperatures))
                    