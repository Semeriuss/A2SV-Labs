from typing import List
from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:  
        frequency = defaultdict(list)
        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c) - ord('a')] += 1
            sortedString = []
            for i in range(26):
                sortedString.append(chr(i + ord('a')) * count[i])
            frequency["".join(sortedString)].append(word)
        return frequency.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs))
                


        