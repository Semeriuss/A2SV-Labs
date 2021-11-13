def mishaAndChangingHandles(edgeList):
    graph = {}
    children = set()
    for parent, child in edgeList:
        graph[parent] = child
        children.add(child)
    
    for handle in graph:        
        while graph[handle] in graph:
            graph[handle] = graph[graph[handle]]
    
    res = {}
    for updated in graph:
        if updated not in children:
            res[updated] = graph[updated]
    
    ret = [f'{k} {v}' for k, v in res.items()]

    return ret

# edgeList = [["Misha", "ILoveCodeForces"], 
#             ["Vasya", "Petrov"], 
#             ["Petrov", "VasyaPetrov123"], 
#             ["ILoveCodeForces", "MikeMirzyanov"],
#             ["Petya", "Ivanov"]]

# print(mishaAndChangingHandles(edgeList))

if __name__ == "__main__":
    n = int(input())
    edgeList = []
    for _ in range(n):
        edgeList.append(list(input().split()))
    
    ret = mishaAndChangingHandles(edgeList)
    print(len(ret))
    print(*ret, sep= "\n")
    
