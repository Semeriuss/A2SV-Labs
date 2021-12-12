from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set(["+", "-", "*", "/"])
        
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            elif token in ops:
                if len(stack) >= 2:
                    right, left = stack.pop(), stack.pop()
                    if token == '/': res = int(float(left)/right)
                    elif token == '+': res = left + right
                    elif token == '-': res = left - right
                    else: res = left * right
                    stack.append(res)
        return stack.pop()
        
        

tokens = ["2","1","+","3","*"]
print(Solution().evalRPN(tokens))