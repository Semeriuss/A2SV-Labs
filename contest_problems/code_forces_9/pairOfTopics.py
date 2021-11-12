def pairOfTopics(teacherInterest, studentInterest):

    n = len(teacherInterest)
    goodness = [0] * n
    for i in range(len(teacherInterest)):
        goodness[i] = teacherInterest[i] - studentInterest[i]

    goodness.sort()
    sp = 0
    ep = n - 1
    goodPairs = 0
    while sp < ep:
        if goodness[ep] + goodness[sp] > 0:
            goodPairs += ep - sp
            ep -= 1
        else:
            sp += 1

    return goodPairs
    
if __name__ == "__main__":
    n = int(input())
    teacherInterest = list(map(int, input().split()))
    studentInterest = list(map(int, input().split()))
    print(pairOfTopics(teacherInterest, studentInterest))
