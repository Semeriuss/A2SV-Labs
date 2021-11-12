def pairOfTopics(teacherInterest, studentInterest):

    n = len(teacherInterest)
    goodness = [0] * n
    for i in range(len(teacherInterest)):
        goodness[i] = teacherInterest[i] - studentInterest[i]

    goodness.sort()

    def countFittingPair(target, goodness):
        lower = 0
        upper = len(goodness)

        best = -1
        while lower <= upper:
            mid = (lower + upper)//2
            if goodness[mid] < target:
                lower = mid + 1
            
            elif goodness[mid] > target:
                best = mid
                upper = mid - 1
            
            else:
                lower = mid + 1
        
        return best

    goodPairs = 0
    for i in range(len(goodness)):
        target = -1 * goodness[i]
        goodIndex = countFittingPair(target, goodness[i:]) 
        res = len(goodness[goodIndex:])
        print(goodness[i],"good", target, goodIndex, res)
        goodPairs += res if res > 0 else 0
    return goodPairs

ti = [4, 8, 2, 6, 2]
si = [4, 5, 4, 1, 3]

res = [-2, -1, 0,  3, 5]
print(pairOfTopics(ti, si))
    
