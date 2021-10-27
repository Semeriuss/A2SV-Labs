from typing import List
from collections import deque

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:

        edgeList = [[] for _ in range(len(parents))]

        for i, node in enumerate(parents):
            if node >= 0:
                edgeList[node].append(i) 
        
        max_count, max_val = 0, 0
        def dfs(root):
            nonlocal max_count, max_val, parents
            children = [dfs(child) for child in edgeList[root]]
            result = 1 + sum(children)

            remainingUpperNodes = len(parents) - result
            product = max(remainingUpperNodes, 1)
            for childCount in children:
                product *= childCount
            
            if max_val < product:
                max_count, max_val = 1, product
            elif max_val == product:
                max_count += 1

            return result
        dfs(0)
        return max_count
    

parents = [-1,2,0,2,0]
parents = [-1,2,0]
print(Solution().countHighestScoreNodes(parents))  
                
                    
                

        