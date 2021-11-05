import heapq
class Solution:
    def solve(self, edges, a, b):
        print(self.MST(edges, a, b), self.MST(edges, a, b, True))
        return self.MST(edges, a, b) == self.MST(edges, a, b, True)

    def MST(self, edges, a, b, withEdgesAdded = False):
        parent = [i for i in range(len(edges) + 1)]
        children = [1 for _ in range(len(edges) + 1)]

        def getParent(node):
            nonlocal parent, children
            if parent[node] == node:
                return node
            parent[node] = getParent(parent[node])
            return parent[node]
        
        def merge(a, b):
            nonlocal parent, children
            a_parent, b_parent = getParent(a), getParent(b)
            if a_parent != b_parent:
                if children[a_parent] > children[b_parent]:
                    children[a_parent] += children[b_parent]
                    parent[b_parent] = a_parent
                else:
                    children[b_parent] += children[a_parent]
                    parent[a_parent] = b_parent
            
        queue = []
        mst_weight = 0
        for edge in edges:
            u, v, w = edge
            if withEdgesAdded and (min(u, v) == min(a, b) and max(u,v) == max(a,b)):
                mst_weight += w
                parent[a] = parent[b]
                children[b] += 2
            else:
                heapq.heappush(queue, (w, u, v))
        
        mst_edge = []
        while queue:
            edge = heapq.heappop(queue)
            w, u, v = edge
            u_parent, v_parent = getParent(u), getParent(v)
            if u_parent != v_parent:
                mst_edge.append((u, v, w))
                mst_weight += w
                merge(u_parent, v_parent)
            
        return mst_weight
            
edges = [
    [0, 1, 100],
    [1, 2, 100],
    [2, 0, 100]
]
a = 0
b = 2

print(Solution().solve(edges, a, b))