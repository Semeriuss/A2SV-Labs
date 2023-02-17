import collections


class Solution:
    # O(N) time and space
    def firstUniqChar(self, s: str) -> int:
        frequency = collections.Counter(s)
        for i, c in enumerate(s):
            if frequency[c] == 1:
                return i
        return -1
