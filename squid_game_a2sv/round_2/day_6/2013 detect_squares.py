from typing import List


class DetectSquares:
    # O(N) time and space

    def __init__(self):
        self.points = {}
        self.ptsList = []

    def add(self, point: List[int]) -> None:
        state = tuple(point)
        self.points[state] = self.points.get(state, 0) + 1
        self.ptsList.append(state)

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0
        for i, j in self.ptsList:
            if abs(i - x) == abs(j - y) and x != i and y != j:
                res += self.points.get((i, y), 0) * self.points.get((x, j), 0)
        return res
