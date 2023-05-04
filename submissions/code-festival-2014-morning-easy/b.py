n = int(input())
m, d = divmod(n, 20)
if d == 0:
    if m % 2 == 0:
        print(1)
    else:
        print(20)
else:
    if m % 2 == 0:
        print(d)
    else:
        print(20 - d + 1)
