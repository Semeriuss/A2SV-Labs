import sys

def trim(edges, v, ops):
    if ops >= v or v == 1:
        return 0
    
    for i in range(ops):
        leaves = [leaf for leaf in edges if edges.count(leaf) == 1]
        for i, leaf in enumerate(leaves):
            if leaf in edges:
                print("index", i, "edges", edges, leaf )
                edges.remove(leaf)
                
                if i < len(edges):
                    if i % 2 == 0:
                        edges.remove(edges[i])
                    else:
                        edges.remove(edges[i - 1])
        
    return len(set(edges))


input = sys.stdin.readline
n = int(input())

input = sys.stdin.readline
empty_line = input()

for i in range(n): 
    input = sys.stdin.readline
    v, ops = list(map(int, input().split()))

    edges = []
    while True:
        input = sys.stdin.readline
        data = input()
        if data == "" or len(data) <= 1:
            break

        else:
            if data == "" or len(data) <= 1:
                break
            else:
                e1, e2 = list(map(int, data.split()))
                edges.append(e1)
                edges.append(e2)
    print("###################")
    print(trim(edges, v, ops))
    print("###################")
    print()

