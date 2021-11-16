def solveMaze(maze):
    ROWSIZE = len(maze)
    COLSIZE = len(maze[0])

    def fitsBoundary(n, m):
        return 0 <= n < ROWSIZE and 0 <= m < COLSIZE

    directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]

    def closePath(graph, source):
        cRow, cCol = source
        for direction in directions:
            sideRow, sideCol = cRow + direction[0], cCol + direction[1]
            if fitsBoundary(sideRow, sideCol):   
                cCell = graph[sideRow][sideCol]
                if (cCell == "."):
                    graph[sideRow][sideCol] = "#"
                elif cCell == "G": 
                    return False
        return True

    def hasPath(graph, src, dst, visited):
        if src == dst: return True
        sRow, sCol = src
        visited.add(src)
        for x, y in directions:
            nRow, nCol = sRow + x, sCol + y
            if fitsBoundary(nRow, nCol) and \
                graph[nRow][nCol] != "#" and \
                graph[nRow][nCol] != "B" and \
                (nRow, nCol) not in visited and \
                hasPath(graph, (nRow, nCol), dst, visited): return True
        return False 

    target = (ROWSIZE - 1, COLSIZE - 1)
    goods = []
    for i in range(ROWSIZE):
        for j in range(COLSIZE):
            cCell = maze[i][j]
            if cCell == "B":
                if not closePath(maze, (i, j)):
                    return "No"
            elif cCell == "G":
                goods.append((i, j))
    

    if maze[ROWSIZE - 1][COLSIZE - 1] != "#" and len(goods) == 0:
        return "YES"

    pathExists = True
    for good in goods:
        if not hasPath(maze, good, target, set()):
            pathExists = False
            break
    return "YES" if pathExists else "NO"    

if __name__ == "__main__":
    t = int(input())
    res = []
    for _ in range(t):
        maze = []
        n, m = map(int, input().split())
        for _ in range(n):
            maze.append(list(input()))
        res.append(solveMaze(maze))
    print(*res, sep="\n")

