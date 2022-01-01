from typing import List
from collections import defaultdict

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:

        root = list(range(n))
        size = [1] * (n)

        restrictedset = set()
        for node1, node2 in restrictions:
            restrictedset.add(node1)
            restrictedset.add(node2) 

        def find(node):
            if node != root[node]:
                root[node] = find(root[node])
            return root[node]
        
        def union(node1, node2):
            smallroot, bigroot = (find(node1), find(node2))if find(node2) in restrictedset else (find(node2), find(node1))
            root[smallroot] = bigroot
            size[bigroot] += size[smallroot]
        
        def notRestricted(node1, node2):
            for restriction in restrictions:
                rest1, rest2 = restriction
                root1, root2 = find(node1), find(node2)
                if min(root1, root2) == min(rest1, rest2) and max(root1, root2) == max(rest1, rest2):
                    return False
            return True

        res = []
        for request in requests:
            node1, node2 = request
            # print(root)
            if notRestricted(node1, node2):
                union(node1, node2)
                res.append(True)
            else:
                res.append(False)
            # print(root)
            
        return res
                        

n = 5
restrictions = [[0,1],[1,2],[2,3]]
requests = [[0,4],[1,2],[3,1],[3,4]]

# n = 3
# restrictions = [[0,1]]
# requests = [[1,2],[0,2]]

# n = 3
# restrictions = [[0,1]]
# requests = [[0,2],[2,1]]

n = 8
restrictions = [[6,4],[7,5],[2,6],[1,5],[6,7],[6,5],[0,3],[5,4],[0,4],[2,7],[0,2]]
requests = [[6,3],[0,2],[0,5],[0,3],[6,4],[2,4],[1,0],[2,1],[2,5],[6,7],[7,0],[3,2],[3,5],[2,1],[1,6],[7,4],[6,3],[1,3],[6,5],[3,7],[7,0],[6,5],[0,5],[0,4],[7,5],[7,0],[7,0],[1,3]]
print(Solution().friendRequests(n, restrictions, requests))
