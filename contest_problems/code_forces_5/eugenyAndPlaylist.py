import sys

input = sys.stdin.readline
n, m = tuple(list(map(int, input().split())))

timeAndDuration = []
for i in range(n):
    timeAndDuration.append(tuple(list(map(int, input().split()))))

requiredDuration = list(map(int, input().split()))

def findSong(timeAndDuration, requiredDuration):
    NUMBER_OF_SONGS = len(timeAndDuration)
    eugenyDuration = timeAndDuration[0][0] * timeAndDuration[0][1]

    songIndex, durationIndex = 0, 0
    while durationIndex < len(requiredDuration):
        if requiredDuration[durationIndex] <= eugenyDuration:
            if songIndex > NUMBER_OF_SONGS:
                print((songIndex + 1) % NUMBER_OF_SONGS)
            else:
                print(songIndex + 1)
            durationIndex += 1
        
        else:
            songIndex += 1
            eugenyDuration += timeAndDuration[songIndex][0] * timeAndDuration[songIndex][1]
        
        

findSong(timeAndDuration, requiredDuration)

