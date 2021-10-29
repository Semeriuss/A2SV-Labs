import sys

input = sys.stdin.readline 
a = int(input())
b = int(input())

# 25 minutes ====> 2 tries, 1 - runtime
def minimumTiredness(a, b):
    
    def generateMotion(motion):
        distance, even = motion
        distance = distance//2
        if even:
            return (distance*(distance + 1))
        else:
            return (distance*(distance + 1)//2) + ((distance + 1)*((distance + 1) + 1)//2)

    distance = abs(a - b)
    if distance % 2 == 0:
        motion = distance, True
    else:
        motion = distance, False
    
    res = generateMotion(motion)
    return res

print(minimumTiredness(a, b))
# tests = [(3, 4), (101, 99), (5, 10), (1,1), (1000, 50)]
# for test in tests:
#     a, b = test
#     print(minimumTiredness(a, b))