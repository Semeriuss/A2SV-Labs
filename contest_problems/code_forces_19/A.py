def solve(rating):
    if rating <= 1399:
        return "Division 4"
    elif rating <= 1599:
        return "Division 3"
    elif rating <= 1899:
        return "Division 2"
    else:
        return "Division 1"

    

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print(solve(int(input())))