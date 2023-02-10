from collections import Counter
from typing import List


class Solution:
    # O(N^2) time | O(N) space
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        N = len(img1)
        a1 = [(i, j) for i in range(N) for j in range(N) if img1[i][j]]
        a2 = [(i, j) for i in range(N) for j in range(N) if img2[i][j]]
        cnt = Counter((xa - xb, ya - yb) for xa, ya in a1 for xb, yb in a2)
        return max(cnt.values() or [0])
