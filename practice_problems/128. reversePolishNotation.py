from typing import List
from math import floor, ceil

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set(["+", "-", "*", "/"])
        
        for token in tokens:
            if token not in ops:
                stack.append(token)
            elif token in ops:
                if len(stack) >= 2:
                    val1 = stack.pop()
                    val2 = stack.pop()
                    res = eval(val2 + token + val1)
                    res = floor(res) if res > 0 else ceil(res)
                    stack.append(str(res))
        return int(stack.pop())
        

tokens = ["2","1","+","3","*"]
print(Solution().evalRPN(tokens))