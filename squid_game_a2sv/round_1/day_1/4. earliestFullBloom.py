from typing import List


class Solution:
    # O(N) time | O(1) space
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        pairs = sorted([(gt, pt)
                       for gt, pt in zip(growTime, plantTime)], reverse=True)
        res = time = 0
        for gTime, pTime in pairs:
            time += pTime
            res = max(res, time + gTime)

        return res
