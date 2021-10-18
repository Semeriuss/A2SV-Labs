def countNegatives(matrix):
    n = len(matrix)
    count = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] < 0:
                count += 1
    return count
                
def positiveMatrixSum(matrix):
    n = len(matrix)
    total = 0
    for i in range(n):
        for j in range(n):
            total += abs(matrix[i][j])
    print(total)
    return total

def minPositiveVal(matrix):
    negativeFlag = False
    n = len(matrix)
    minVal = abs(matrix[0][0])
    for i in range(n):
        for j in range(n):
            if matrix[i][j] < 0: negativeFlag = True
            if abs(matrix[i][j]) < minVal:
                minVal = abs(matrix[i][j])
    
    return minVal if negativeFlag else 0
            
def maxMatrixSum(matrix):
    negativeNums = countNegatives(matrix)
    if negativeNums % 2 == 0:
        return positiveMatrixSum(matrix)
    else:
        return positiveMatrixSum(matrix) - 2 * minPositiveVal(matrix)


tests = [([[1,2,3],[-1,-2,-3],[1,2,3]], 16),
         ([[1,-1],[-1,1]], 4),
         ([[-1,0,-1],[-2,1,3],[3,2,2]], 15),
         ([[10000,10000,10000],[10000,10000,10000],[10000,10000,10000]], 90000),
         ([[9,-3,-4],[-4,-1,-3],[-6,-3,-3]], 36)]
for test in tests:
    matrix, expectedSum = test
    actualSum = maxMatrixSum(matrix)
    print(actualSum == expectedSum, actualSum, expectedSum)
