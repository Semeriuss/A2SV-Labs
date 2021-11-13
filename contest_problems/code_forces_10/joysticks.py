def joysticks(a, b):
    if a <= 0 or b <= 0:
        return 0
    
    elif a == b == 1:
        return 0
        
    else:
        if a < b:
            return 1 + joysticks(a + 1, b - 2)
        
        else:
            return 1 + joysticks(a - 2, b + 1)

if __name__ == "__main__":
    a, b = list(map(int, input().split()))
    print(joysticks(a, b))