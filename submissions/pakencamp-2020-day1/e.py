X, Y = map(int, input().split())

if X == 0 and Y == 0:
    print(1, 1)
elif X == Y:
    print(-1)
elif X < Y:
    print(X + 2 * Y, Y)
else:
    print(X, 2 * X + Y)
