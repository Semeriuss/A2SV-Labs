from typing import List
from collections import Counter, deque

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        res, que = [], deque([])
        for num in sorted(changed):
            if que and que[0] == num:
                que.popleft()
            else:
                que.append(num*2)
                res.append(num)
        return [] if que else res
