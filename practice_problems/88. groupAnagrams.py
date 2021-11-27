from typing import List
from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        root = list(range(len(strs)))
        
        def find(node):
            if root[node] != node:
                root[node] = find(root[node])
            return root[node]
        
        def union(node1, node2):
            root1, root2 = find(node1), find(node2)
            root[root2] = root1
        
        for i in range(len(strs) - 1):
            checker = Counter(strs[i])
            for j in range(i + 1, len(strs)):
                if checker == Counter(strs[j]):
                    union(i, j)
        
        group = defaultdict(list)
        for i, n in enumerate(root):
            group[n].append(strs[i])
    
        return list(group.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs))
                


        