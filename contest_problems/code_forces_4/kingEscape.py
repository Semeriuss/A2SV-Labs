import sys

input = sys.stdin.readline
n = int(input())

input = sys.stdin.readline
queenSquare = tuple(list(map(int, input().split())))

input = sys.stdin.readline
kingSquare = tuple(list(map(int, input().split())))

input = sys.stdin.readline
escapeSquare = tuple(list(map(int, input().split())))

def kingEscape(kingPos, queenPos, escapePos):
    kingX, kingY = kingPos
    queenX, queenY = queenPos
    escapeX, escapeY = escapePos

    canEscape = False

    if (kingX > queenX) and (escapeX > queenX) and (kingY > queenY) and (escapeY > queenY):
        canEscape = True
    if (kingX < queenX) and (escapeX < queenX) and (kingY < queenY) and (escapeY < queenY):
        canEscape = True
    if (kingX > queenX) and (escapeX > queenX) and (kingY < queenY) and (escapeY < queenY):
        canEscape = True
    if (kingX < queenX) and (escapeX < queenX) and (kingY > queenY) and (escapeY > queenY):
        canEscape = True
    
    if canEscape:
        return 'YES'
    return 'NO'

# tests = [((1,3), (4,4), (3,1)),
#          ((2,3), (4,4), (1,6)),
#          ((1,2), (3,5), (6,1)),
#          ((5,0), (1,2), (0,5)),
#          ((0,12), (10,10), (12,12)),
#          ((0,12), (10, 10), (12,0))]
# for test in tests:
#     kingSquare, queenSquare, escapeSquare = test
#     print(kingEscape(kingSquare, queenSquare, escapeSquare))

print(kingEscape(kingSquare, queenSquare, escapeSquare))