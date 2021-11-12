def findMaxConnectableEdges(n, mochaEdges, dianaEdges):
    mochaForest, dianaForest = list(range(n + 1)), list(range(n + 1))
    mochaSize, dianaSize = [1] * (n + 1), [1] * (n + 1)

    def find(node, forest):
        if node != forest[node]:
            forest[node] = find(forest[node], forest)
        return forest[node]

    def union(node1, node2, forest, size):
        smallRoot, bigRoot = sorted([find(node1, forest), find(node2, forest)], key=lambda x: size[x])

        if smallRoot != bigRoot:
            forest[smallRoot] = bigRoot
            size[bigRoot] += size[smallRoot]

    def connected(node1, node2, forest):
        return find(node1, forest) == find(node2, forest)

    for node1, node2 in mochaEdges:
        union(node1, node2, mochaForest, mochaSize)

    for node1, node2 in dianaEdges:
        union(node1, node2, dianaForest, dianaSize)
        
    connectableEdges = []
    for node1 in range(1, n+1):
        mochaRoot = find(node1, mochaForest)
        for node2 in range(1, n+1):
            dianaRoot = find(node2, dianaForest)
            if connected(mochaRoot, dianaRoot, mochaForest) or connected(mochaRoot, dianaRoot, dianaForest):
                continue
            if mochaRoot != dianaRoot:
                connectableEdges.append(f'{node1} {node2}')
                union(mochaRoot, dianaRoot, mochaForest, mochaSize)
                union(mochaRoot, dianaRoot, dianaForest, dianaSize)

    maxConnectableEdges = len(connectableEdges)
    print(maxConnectableEdges)
    if maxConnectableEdges:
        print(*connectableEdges, sep="\n")

if __name__ == "__main__":
    n, m1, m2 = list(map(int, input().split()))
    mochaEdges = []
    for i in range(m1):
        mochaEdges.append(tuple(list(map(int, input().split()))))

    dianaEdges = []
    for j in range(m2):
        dianaEdges.append(tuple(list(map(int, input().split()))))
    
    findMaxConnectableEdges(n, mochaEdges, dianaEdges)
