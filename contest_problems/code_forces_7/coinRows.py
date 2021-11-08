# t = int(input())

# tests = []
# for i in range(t):
#     n = int(input())
#     mat = []
#     for i in range(2):
#         mat.append(list(map(int, input().split())))
    
def coinRows(n, mat):

    target = (1, n - 1)
    paths = []
    source = (0, 0)
    def dfs(graph, source, target, paths):
        x, y = source   
        if x > 1 or y >= n:
            return 0

        if source == target:
            return graph[x][y]

        # print("I'm here,", graph, source, target, paths)
        path1 = dfs(graph, (x, y + 1), target, paths)
        path2 = dfs(graph, (x + 1, y), target, paths)
        if path1 and path2:
            paths.append(max(path1, path2))
        
        elif not path1 and path2:
            pass
        else:
            path = path1 if path1 else path2
            paths.append(path)
    
    maxsum = dfs(mat, source, target, paths)
    print (paths, maxsum)

coinRows(3, [[1,3,7], [3,5,1]])

    

# def dfs(graph, source, target, paths):
#         x, y = source   
#         if x > 1 or y >= n:
#             return 

#         if source == target:
#             return 
            
#         paths.append(dfs(graph, (x, y + 1), target, paths))
#         paths.append(dfs(graph, (x + 1, y), target, paths))
    