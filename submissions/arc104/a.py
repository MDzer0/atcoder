X, Y = map(int, input().split())

for i in range(-100, 101):
    for j in range(-100, 101):
        if i + j == X and i - j == Y:
            print(i, j)
