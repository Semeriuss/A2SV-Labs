
n = 8
root = [i for i in range(n + 1)]
size = [1 for i in range(n + 1)]

def find(node):
    if node != root[node]:
        root[node] = find(root[node])
    return root[node]

def union(node1, node2):
    smallRoot, bigRoot = sorted([find(node1), find(node2)], key=lambda x: size[x])
    if smallRoot != bigRoot:
        root[smallRoot] = bigRoot
        size[bigRoot] += size[smallRoot]

def connected(node1, node2):
    return find(node1) == find(node2)

union(3, 4)
print(find(3))
    