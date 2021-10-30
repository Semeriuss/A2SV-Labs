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

    canEscape = True

    if ((kingX > queenX) and (queenX > escapeX)) or ((escapeX > queenX) and (queenX > kingX)):
        canEscape = False
    if ((kingY > queenY) and (queenY > escapeY)) or ((escapeY > queenY) and (queenY > kingY)):
        canEscape = False
    
    if canEscape:
        return 'YES'
    return 'NO'

# tests = [((1,3), (4,4), (3,1)),
#          ((2,3), (4,4), (1,6)),
#          ((1,2), (3,5), (6,1))]
# for test in tests:
#     kingSquare, queenSquare, escapeSquare = test
#     print(kingEscape(kingSquare, queenSquare, escapeSquare))

print(kingEscape(kingSquare, queenSquare, escapeSquare))