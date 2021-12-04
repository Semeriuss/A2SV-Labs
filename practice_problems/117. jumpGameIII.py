from typing import List
from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        canJump = False
        N = len(arr)

        def fitsBoundary(index):
            return 0 <= index < N

        que = deque([start])
        visited = set()
        while que:
            curr_pos = que.popleft()

            if fitsBoundary(curr_pos) and not arr[curr_pos]:
                canJump = True
                break
            
            if fitsBoundary(curr_pos) and (curr_pos, arr[curr_pos]) not in visited:
                visited.add((curr_pos, arr[curr_pos]))
                que.append(curr_pos + arr[curr_pos])
                que.append(curr_pos - arr[curr_pos])
            
        return canJump
        
