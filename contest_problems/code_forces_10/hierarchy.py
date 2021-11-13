from collections import defaultdict
import heapq
def hierarchy(n, edgeList):
    root = list(range(n+1))
    size = [1] * (n + 1)


    def find(node):
        # if root[node] != node:
        #     root[node] = find(root[node])
        # return root[node]
        if root[node] == node:
            return node
        root[node] = find(root[node])
        return root[node]

    def union(node1, node2):
        root1, root2 = find(node1), find(node2)
        root[root2] = root1
        size[root1] += size[root2]
    
    def connected(node1, node2):
        return find(node1) == find(node2)
    
    heapq.heapify(edgeList)
    
    cost = 0
    supervised = set()
    rootFinder = 0
    while edgeList:
        edgeCost, edge1, edge2 = heapq.heappop(edgeList)
        if not connected(edge1, edge2) and edge2 not in supervised:
            cost += edgeCost
            union(edge1, edge2)
            supervised.add(edge2)
        rootFinder = edge1
    root = find(rootFinder)
    finalSize = size[root]
    if finalSize != n:
        return -1
    else:
        return cost

if __name__ == "__main__":
    n = int(input())
    qualifications = list(map(int, input().split()))
    m = int(input())
    if n == 1:
        print(0)
    else:
        edgeList = []
        for _ in range(m):
            edge1, edge2, cost = map(int, input().split())
            edgeList.append((cost, edge1, edge2))
        print(hierarchy(n, edgeList))

