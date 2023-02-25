n, m = map(int, input().split())
color = set(['C', 'Y', 'M'])
photo = set()
for _ in range(n):
    for c in list(input().split()):
        photo.add(c)
if color.intersection(photo):
    print('#Color')
else:
    print('#Black&White')
