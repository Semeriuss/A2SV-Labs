from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stack = [len(temperatures) - 1]
        for i in range(len(temperatures) - 1, - 1, -1):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                stack.pop()
            if stack: answer[i] = stack[-1] - i
            stack.append(i)
                
        return answer

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(Solution().dailyTemperatures(temperatures))
                    