import sys

input = sys.stdin.readline
positions = list(map(int, input().split()))

currentPosition, nextPosition = (positions[0], positions[1]), (positions[2], positions[3])

def rookBishopKing(currentPos, nextPos):
    x1, y1 = currentPos
    x2, y2 = nextPos

    rookSteps, bishopSteps, kingSteps = 0, 0, 0

    def getRookSteps():
        nonlocal rookSteps

        if x1 == x2 or y1 == y2:
            rookSteps = 1
        else:
            rookSteps = 2

        return rookSteps
    
    def getBishopSteps():
        nonlocal bishopSteps

        if ((x1 + y1) % 2) != ((x2 + y2) % 2):
            bishopSteps = 0
        else:
            if (x2 - x1) != 0 and ((y2 - y1)/(x2 - x1) == 1 or (y2 - y1)/(x2 - x1) == -1):
                bishopSteps = 1
            else:
                bishopSteps = 2

        return bishopSteps
    
    def getKingSteps():
        nonlocal kingSteps

        kingSteps = max(abs(y2 - y1), abs(x2 - x1))

        return kingSteps

    
    rookSteps, bishopSteps, kingSteps = getRookSteps(), getBishopSteps(), getKingSteps()
    
    return f'{rookSteps} {bishopSteps} {kingSteps}'

print(rookBishopKing(currentPosition, nextPosition))


    

    