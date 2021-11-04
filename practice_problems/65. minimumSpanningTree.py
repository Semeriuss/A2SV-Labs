import heapq
from collections import deque
class Solution:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.children = [1 for _ in range(n + 1)]

    def solve(self, edges, a, b):
        return self.MST(edges, a, b)

    def MST(self, edges, a, b):

        def getParent(node):
            if self.parent[node] == node:
                return node
            self.parent[node] = getParent(self.parent[node])
            return self.parent[node]
        
        def merge(a, b):
            a_parent, b_parent = getParent(a), getParent(b)
            if a_parent != b_parent:
                if self.children[a_parent] > self.children[b_parent]:
                    self.children[a_parent] += self.children[b_parent]
                    self.parent[b_parent] = a_parent
                else:
                    self.children[b_parent] += self.children[a_parent]
                    self.parent[a_parent] = b_parent
            
        queue = []
        for edge in edges:
            u, v, w = edge
            heapq.heappush(queue, (w, u, v))
        
        mst_edge = []
        while queue:
            edge = heapq.heappop(queue)
            w, u, v = edge
            u_parent, v_parent = getParent(u), getParent(v)
            if u_parent != v_parent:
                mst_edge.append((u, v, w))
                merge(u, v)
            
        return mst_edge
            
edges = [
    [0, 1, 100],
    [1, 2, 100],
    [2, 0, 300]
]
a = 0
b = 2

print(Solution(len(edges)).solve(edges, a, b))