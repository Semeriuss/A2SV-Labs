n = int(input())
percentage = list(map(int, input().split()))

res = 0
for percent in percentage:
    res += (percent/100)

res /= n 

res *= 100

print(f"{res:.14}")