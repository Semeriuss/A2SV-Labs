from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        root = list(range(len(isConnected)))
        size = [1] * len(isConnected)

        def find(node):
            if node != root[node]:
                root[node] = find(root[node])
            return root[node]
        
        def union(node1, node2):
            root1, root2 = sorted([find(node1), find(node2)], key=lambda x: size[x])
            root[root1] = root2
            size[root2] += size[root1]
        
        def rootConnected(node1, node2):
            return find(node1) == find(node2)
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i != j and (isConnected[i][j] or rootConnected(i, j)):
                    union(i, j)
        print(root)
        return len(set(root))

isConnected = [
                [1,1,1,0,1,1,1,0,0,0],
                [1,1,0,0,0,0,0,1,0,0],
                [1,0,1,0,0,0,0,0,0,0],
                [0,0,0,1,1,0,0,0,1,0],
                [1,0,0,1,1,0,0,0,0,0],
                [1,0,0,0,0,1,0,0,0,0],
                [1,0,0,0,0,0,1,0,1,0],
                [0,1,0,0,0,0,0,1,0,1],
                [0,0,0,1,0,0,1,0,1,1],
                [0,0,0,0,0,0,0,1,1,1]
            ]

isConnected = [
                [1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],
                [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],
                [0,0,0,0,1,0,0,0,0,1,1,0,0,0,0],
                [0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],
                [0,0,0,1,0,0,1,0,1,0,0,0,0,1,0],
                [1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
                [0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],
                [0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],
                [0,0,0,0,1,1,0,0,0,0,1,1,0,0,0],
                [0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],
                [0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]
            ]
print(Solution().findCircleNum(isConnected))