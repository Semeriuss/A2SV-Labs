def newProblem(names):

    def subsets(A):
        if A == []:
            return [[]]
        sub = subsets(A[:-1])
        return sub + [rem + [A[-1]] for rem in sub]

    visited = set([])
    for name in names: 
        parts = subsets(list(name))
        for c in parts:
            visited.add("".join(c))
    
    newName = [chr(ord('a'))]
    while "".join(newName) in visited:
        currentName = newName[:]
        for i in range(26):
            currentName[-1] = chr(ord('a') + i)
            if "".join(currentName) not in visited: 
                return "".join(currentName)
        newName.append(chr(ord('a')))
    return "".join(newName)

if __name__ == "__main__":
    n = int(input())
    names = []
    for _ in range(n): names.append(input())
    print(newProblem(names))