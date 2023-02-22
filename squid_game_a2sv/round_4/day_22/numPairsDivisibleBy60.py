from collections import defaultdict
from typing import List


class Solution:
    # O(n) time | O(n) space
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        rem = defaultdict(int)
        count = 0
        for t in time:
            count += rem[-t % 60]
            rem[t % 60] += 1
        return count
