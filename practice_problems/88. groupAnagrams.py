from typing import List
from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:  
        frequency = defaultdict(list)
        for word in strs:
            frequency["".join(sorted(word))].append(word)
        return frequency.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs))
                


        