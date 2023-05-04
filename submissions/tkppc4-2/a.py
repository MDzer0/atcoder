x, y = map(int, input().split())
m, d = divmod(y, 2)
if d == 1:
    print(-1)
    exit()

if m % 2 == 0:
    if abs(x) <= m:
        print(m)
    else:
        print(-1)
else:
    if abs(x) % 2 != 0:
        if abs(x) <= m:
            print(m)
        else:
            print(-1)
    else:
        print(-1)
