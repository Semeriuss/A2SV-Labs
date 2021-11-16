import sys
sys.setrecursionlimit(3000)
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
    c = 0
    def countGoods(graph, src, visited, count):
        nonlocal c
        sRow, sCol = src
        visited.add(src)
        for x, y in directions:
            nRow, nCol = sRow + x, sCol + y
            if fitsBoundary(nRow, nCol) and graph[nRow][nCol] != "#" and (nRow, nCol) not in visited:
                visited.add((nRow, nCol))
                if graph[nRow][nCol] == "G":
                    c += 1
                    countGoods(graph, (nRow, nCol), visited, count)
                else:
                    countGoods(graph, (nRow, nCol), visited, count)
        return c

    target = (ROWSIZE - 1, COLSIZE - 1)
    goodCount = 0
    for i in range(ROWSIZE):
        for j in range(COLSIZE):
            cCell = maze[i][j]
            if cCell == "B":
                if not closePath(maze, (i, j)):
                    return "NO"
            elif cCell == "G":
                goodCount += 1
    
    if maze[ROWSIZE - 1][COLSIZE - 1] != "#" and goodCount == 0:
        return "YES"
    elif maze[ROWSIZE - 1][COLSIZE - 1] == "#" and goodCount > 0:
        return "NO"
    
    
    count = countGoods(maze, target, set(), c)
    return "YES" if count == goodCount else "NO"    

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

