def matrixBlockSum(mat, k):
    pass

def matrixPrefixSum(mat):
    prefixSum = [[0 for _ in range(len(mat[0])) for _ in range(len(mat))]]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i - 1 > 0 and j - 1 < 0:
                prefixSum[i][j] = prefi
                
