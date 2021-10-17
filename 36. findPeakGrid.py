def findPeakGrid(mat):
    peak = mat[0][0]
    peakPoint = (0,0)
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] > peak:
                peak = mat[i][j]
                peakPoint = i,j

    return list(peakPoint)

def findPeakGrid(mat):
    

tests = [([[1,4],[3,2]], [0,1], [1,0]),
         ([[10,20,15],[21,30,14],[7,16,32]],[1,1],[2,2])]

for test in tests:
    if len(test) == 2:
        mat, expected = test
    elif len(test) == 3:
        mat, expected, expected2 = test
    actual = findPeakGrid(mat)
    print(actual == expected or actual == expected2)
         
