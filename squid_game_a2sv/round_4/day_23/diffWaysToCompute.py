from functools import lru_cache
from typing import List


class Solution:
    # Catalan Number?
    @lru_cache()
    def diffWaysToCompute(self, expr: str) -> List[int]:
        if expr.isdigit():
            return [int(expr)]
        res = []
        for i, c in enumerate(expr):
            if c in '*+-':
                leftWays = self.diffWaysToCompute(expr[:i])
                rightWays = self.diffWaysToCompute(expr[i+1:])
                for left in leftWays:
                    for right in rightWays:
                        if c == '*':
                            res.append(left * right)
                        elif c == '+':
                            res.append(left + right)
                        else:
                            res.append(left - right)
        return res
