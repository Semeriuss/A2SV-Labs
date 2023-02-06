from collections import deque


class Solution:
    # O(LogN) space and time, where N is the target (height of tree)
    def racecar(self, target: int) -> int:
        pos, speed = 0, 1
        que = deque([(0, pos, speed)])
        seen = set()
        while que:
            steps, curPos, curSpeed = que.popleft()
            if curPos == target:
                return steps
            if (curPos, curSpeed) in seen:
                continue
            seen.add((curPos, curSpeed))
            que.append((steps + 1, curPos + curSpeed, curSpeed*2))
            que.append((steps + 1, curPos, -1 if curSpeed > 0 else 1))
