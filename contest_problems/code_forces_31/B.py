n, m = map(int, input().split())
polandBall = set()
enemyBall = set()
common = set()
for _ in range(n):
    polandBall.add(input())
for _ in range(m):
    s = input()
    if s in polandBall:
        common.add(s)
    enemyBall.add(s)


if len(polandBall) > len(enemyBall):
    print("YES")
elif len(enemyBall) > len(polandBall):
    print("NO")
else:
    print("YES" if len(common) % 2 == 1 else "NO")
    