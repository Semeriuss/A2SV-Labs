def armChairs(seats):
    ones, zeros = [], []
    minutes = 0

    for i, seat in enumerate(seats):
        if seat == 1:
            ones.append(i)
        else:
            zeros.append(i)
    
    for i in range(len(ones)):
        minutes += abs(ones[i] - zeros[i])
    
    return minutes

def armChairs(seats):
    sp, ep = 0, 0
    minutes = 0
    
    while ep < len(seats):
        if seats[sp] == seats[ep]:
            ep += 1
        elif seats[sp] != seats[ep]:
            minutes += ep - sp 
            sp +=  1
            ep +=  1
        
        
    
    return minutes
if __name__ == "__main__":
    n = int(input())
    seats = list(map(int, input().split()))
    print(armChairs(seats))