
def joysticks(a, b):
    if a <= 0 or b <= 0:
        return 0
    
    else:
        # return 1 + max(joysticks(a + 1, b - 2), joysticks(a - 2, b + 1))
        if a < b:
            return 1 + joysticks(a + 1, b - 2)
        
        else:
            return 1 + joysticks(a - 2, b + 1)



if __name__ == "__main__":
    a, b = list(map(int, input().split()))
    print(joysticks(a, b))

# def joysticks(a, b):
#     if a <= 0 or b <= 0:
#         return 0
    
#     else:
#         return 1 + max(joysticks(a + 1, b - 2), joysticks(a - 2, b + 1))

# if __name__ == "__main__":
#     a, b = list(map(int, input().split()))
#     print(joysticks(a, b))