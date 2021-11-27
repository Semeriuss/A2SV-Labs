from typing import List
from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:  
        frequency = defaultdict(list)
        for i in range(len(strs)):
            count = [0]*26
            for j in strs[i]:
                count[ord(j) - ord('a')] += 1
            frequency[tuple(count)].append(strs[i])
        return frequency.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs))
                


        