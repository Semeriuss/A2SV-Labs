from functools import cache


for _ in range(int(input())):
    col = int(input())
    row = []
    row.append(list(map(int, list(input()))))
    row.append(list(map(int, list(input()))))

    def isInBound(i, j):
        return i >= 0 and i < 2 and j >= 0 and j < col

    @cache
    def hasPath(i, j):
        if not isInBound(i, j) or row[i][j] == 1:
            return False
        if j == col - 1:
            return True
        return hasPath(i, j + 1) or hasPath(i + 1, j + 1) or hasPath(i - 1, j + 1)

    if hasPath(0, 0):
        print('YES')
    else:
        print('NO')
