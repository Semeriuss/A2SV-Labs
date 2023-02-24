from typing import List


class Solution:
    # O(N) time and O(k) space
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        totalArea = tickets[k] * n
        for i in range(n):
            totalArea -= (tickets[k] - min(tickets[k], tickets[i]))

        for i in range(k + 1, n):
            if tickets[i] >= tickets[k]:
                totalArea -= 1
        return totalArea
