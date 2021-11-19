from typing import List
from collections import defaultdict

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:

        def hasPath(graph, src, dst, visited):
            if src == dst: return True
            visited.add(src)
            for neighbor in graph[src]:
                if neighbor not in visited and hasPath(graph, neighbor, dst, visited): return True
                visited.add(neighbor)
            return False

        def notRestricted(friends):
            for restriction in restrictions:
                node1, node2 = restriction
                if hasPath(friends, node1, node2, set()):
                    return False
            return True

        res = []
        friends = defaultdict(list)
        for request in requests:
            node1, node2 = request
            friends[node1].append(node2)
            friends[node2].append(node1)
            if notRestricted(friends):
                res.append(True)
            else:
                res.append(False)
                friends[node1].remove(node2)
                friends[node2].remove(node1)
        return res
                        

n = 5
restrictions = [[0,1],[1,2],[2,3]]
requests = [[0,4],[1,2],[3,1],[3,4]]

n = 3
restrictions = [[0,1]]
requests = [[1,2],[0,2]]

n = 3
restrictions = [[0,1]]
requests = [[0,2],[2,1]]

print(Solution().friendRequests(n, restrictions, requests))
