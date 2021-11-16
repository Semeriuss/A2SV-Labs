def tableDecoration(r, g, b):
    return min((r + g + b)//3, r+g, g+b, r+b)

def tableDecoration(r, g, b):
    colors = sorted([r, g, b], reverse=True)

    def checkValidity(mid):
        if mid == 0:
            mid = 1
        rounds, remaining = 0, 0
        for color in colors:
            r, rem = divmod(remaining + color, mid)
            remaining = rem * (r < 2)
            rounds += min(2, r)
        return rounds

    lower = 0
    upper = max(r, g, b)
    best = 0
    while lower <= upper:
        mid = (lower + upper)//2
        valid = checkValidity(mid)
        if valid < 3:
            upper = mid - 1
        else:
            best = mid
            lower = mid + 1
    return best
  
if __name__ == "__main__":
    r, g, b = map(int, input().split())
    print(tableDecoration(r, g, b))