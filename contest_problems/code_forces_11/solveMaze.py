from collections import deque
# import sys
# sys.setrecursionlimit(100000)
def solveMaze(maze):
    ROWSIZE = len(maze)
    COLSIZE = len(maze[0])

    def fitsBoundary(n, m):
        return 0 <= n < ROWSIZE and 0 <= m < COLSIZE

    directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    badMeetsGood = False
    def closePath(graph, source):
        cRow, cCol = source
        for direction in directions:
            sideRow, sideCol = cRow + direction[0], cCol + direction[1]
            if fitsBoundary(sideRow, sideCol):
                cCell = graph[sideRow][sideCol]
                if (cCell == "."):
                    graph[sideRow][sideCol] = "#"
                elif cCell == "G":
                    badMeetsGood == True
                    # closePath(graph, (sideRow, sideCol))

    def hasPath(graph, src, dst):
        if src == dst: return True
        sRow, sCol = src
        for neighbor in directions:
            nRow, nCol = sRow + neighbor[0], sCol + neighbor[1]
            if fitsBoundary(nRow, nCol) and \
                graph[nRow][nCol] != "#" and \
                hasPath(graph, (nRow, nCol), dst): return True
        return False 

    target = (ROWSIZE - 1, COLSIZE - 1)
    goods = []
    for i in range(ROWSIZE):
        for j in range(COLSIZE):
            cCell = maze[i][j]
            if cCell == "B":
                closePath(maze, (i, j))
            elif cCell == "G":
                goods.append((i, j))
    
    if badMeetsGood:
        return "No"

    if maze[ROWSIZE - 1][COLSIZE - 1] != "#" and len(goods) == 0:
        return "YES"
    print(maze)
    pathExists = True
    for good in goods:
        if not hasPath(maze, good, target):
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


