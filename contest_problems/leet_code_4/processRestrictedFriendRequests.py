from typing import List
from collections import defaultdict

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        

        root = list(range(n + 1))
        size = [1] * (n + 1)
        
        def notRestricted(edge1, edge2, enemies, friends):
            if edge1 in enemies and edge2 in enemies[edge1]:
                return False
            if edge2 in enemies and edge1 in enemies[edge2]:
                return False
            
            if edge1 in friends:
                for friend in friends[edge1]:
                    if edge2 in enemies[friend]:
                        return False
            
            if edge2 in friends:
                for friend in friends[edge2]:
                    if edge1 in enemies[friend]:
                        return False
            
            return True
            

        res = []
        enemies = defaultdict(list)
        friends = defaultdict(list)
        for restriction in restrictions:
            edge1, edge2 = restriction
            enemies[edge1].append(edge2)
            enemies[edge2].append(edge1)
        
        
        for i, request in enumerate(requests):
            edge1, edge2 = request
            if not notRestricted(edge1, edge2, enemies, friends):
                res.append(False)
            else:
                res.append(True)
                friends[edge1].append(edge2)
                friends[edge2].append(edge1)
                for enemy in enemies[edge2]:
                    if enemy not in enemies[edge1]:
                        enemies[edge1].append(enemy)
                for enemy in enemies[edge1]:
                    if enemy not in enemies[edge2]:
                        enemies[edge2].append(enemy)
        print(enemies, friends, sep="\n")
        return res
                        

n = 5
restrictions = [[0,1],[1,2],[2,3]]
requests = [[0,4],[1,2],[3,1],[3,4]]

print(Solution().friendRequests(n, restrictions, requests))
