from collections import Counter, defaultdict
from typing import List


class Solution:
    # O(n) time | O(n) space
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        res = [0] * k
        hm = defaultdict(set)
        for user, time in logs:
            hm[user].add(time)

        uam = Counter(len(times) for times in hm.values())

        for k, v in uam.items():
            res[k - 1] = v

        return res
