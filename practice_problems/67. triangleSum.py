def triangleSum(triangle, x, y, memo):

    if (x, y) in memo:
        return memo[(x, y)]

    if x < len(triangle) - 1:    
        memo[(x, y)] = triangle[x][y] + max(triangleSum(triangle, x + 1, y, memo), triangleSum(triangle, x + 1, y + 1, memo))
        return memo[(x, y)]

    return triangle[x][y]

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(triangleSum(triangle, 0, 0, {}))