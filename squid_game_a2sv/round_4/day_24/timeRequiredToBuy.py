from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # O(max(tickets)) time | O(1) space
        time = 0
        i = 0
        while tickets[k] != 0:
            if i >= len(tickets):
                i = 0

            if tickets[i] == 0 and i == k:
                break

            if tickets[i] > 0:
                tickets[i] -= 1
                time += 1
                i += 1

            elif tickets[i] == 0:
                i += 1

        return time
