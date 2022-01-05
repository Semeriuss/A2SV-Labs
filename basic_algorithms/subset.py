def subset(A):
    if A == []:
        return [[]]
    sub = subset(A[:-1])
    return sub + [rem + [A[-1]] for rem in sub]

tests = [[], [1], [1,2], [1,2,3]]
for test in tests:
    print(subset(test))