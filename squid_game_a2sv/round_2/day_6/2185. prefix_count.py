from typing import List


class Solution:
    # O(M*N) time and O(1) space where M is length of prefix and N is the length of the array
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(int(word.startswith(pref)) for word in words)
