import sys

input = sys.stdin.readline
nStairs = int(input())

input = sys.stdin.readline
stairs = list(map(int,input().split()))

input = sys.stdin.readline
nBoxes = int(input())

boxes = []
for i in range(nBoxes):
    input = sys.stdin.readline
    boxes.append((list(map(int,input().split()))))

stair_pos = 0
box_pos = 0

currentHeight = stairs[stair_pos]
maxStairHeight = stairs[-1]
while box_pos < nBoxes:
    w, h = boxes[box_pos]
    
    # print("w",w, " ","sp ", stair_pos + 1)
    if w > stair_pos + 1:
        stair_pos += 1
        currentHeight = max(stairs[stair_pos], currentHeight)
    
    else:
        print(currentHeight)
        box_pos += 1
        currentHeight += h
        
