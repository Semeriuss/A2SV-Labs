from collections import deque
from typing import List


class Solution:
    # O(n) time and space
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        res = []
        que = deque([])

        for num in changed:
            if que and num == que[0]:
                que.popleft()
            else:
                que.append(num * 2)
                res.append(num)

        if que:
            return []
        return res
