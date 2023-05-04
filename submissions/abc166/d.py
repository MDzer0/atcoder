X = int(input())

for i in range(1001):
    for j in range(-1000, 1001):
        if pow(i, 5) - pow(j, 5) == X:
            print(i, j)
            exit()
