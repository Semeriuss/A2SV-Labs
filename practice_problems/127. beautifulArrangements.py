from typing import List


class Solution:
    def countArrangement(self, n: int) -> int:
        return self.bitMaskCount(n, 0, n)
    
    def bitMaskCount(self, N: int, bitmask: int, index: int):
        if index == 0: return 1
        order = 0
        for i in range(N):
            if not bitmask&1<<i and (not (i + 1)%index or not index%(i + 1)):
                order += self.bitMaskCount(N, bitmask^1<<i, index - 1)
        return order

print(Solution().countArrangement(15))