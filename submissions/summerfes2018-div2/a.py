x, y, z = map(int, input().split())

for i in range(2, 10 ** 5 + 1):
    tx = y - z
    ty = z - x
    tz = x - y
    if tx == 0 or ty == 0 or tz == 0:
        print(i)
        exit()
    x = tx
    y = ty
    z = tz

print(-1)
