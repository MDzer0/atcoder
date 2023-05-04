n, x = map(int, input().split())

y = int(n / 2)
if y >= x:
    print(x - 1)
else:
    print(n - x)
