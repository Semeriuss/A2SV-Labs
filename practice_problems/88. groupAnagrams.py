from typing import List
from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        root = list(range(len(strs)))
        group = []
        visited = set()
        for i in range(len(strs)):
            if i not in visited:
                visited.add(i)
                checker = Counter(strs[i])
                temp = [strs[i]]
                for j in range(i, len(strs)):
                    if j not in visited:
                        if checker == Counter(strs[j]):
                            temp.append(strs[j])
                            visited.add(j)
                group.append(temp)
    
        return group


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs))
                


        