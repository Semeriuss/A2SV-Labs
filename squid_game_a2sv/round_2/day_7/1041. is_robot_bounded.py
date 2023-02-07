class Solution:
    # O(N) time | O(1) space
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, dx, dy = 0, 0, 0, 1
        for i in instructions:
            if i == "L":
                dx, dy = -dy, dx
            elif i == "R":
                dx, dy = dy, -dx
            elif i == "G":
                x, y = x + dx, y + dy
        return (x, y) == (0, 0) or (dx, dy) != (0, 1)
