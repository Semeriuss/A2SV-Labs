def tableDecoration(r, g, b):
    return min((r + g + b)//3, r+g, g+b, r+b)

if __name__ == "__main__":
    r, g, b = map(int, input().split())
    print(tableDecoration(r, g, b))