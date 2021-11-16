def armChairs(seats):
    sp, ep = 0, 0
    minutes = 0
    while ep < len(seats):
        if seats[sp] == seats[ep] == 1:
            ep += 1
        elif seats[sp] == seats[ep] == 0:
            ep += 1
            sp += 1
        else:
            minutes += (ep - sp)
            sp += 1
            ep += 1
    return minutes

if __name__ == "__main__":
    n = int(input())
    seats = list(map(int, input().split()))
    print(armChairs(seats))