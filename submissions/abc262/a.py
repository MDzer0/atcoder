Y = int(input())
tmp = Y % 4
if tmp == 0:
    print(Y + 2)
elif tmp == 1:
    print(Y + 1)
elif tmp == 2:
    print(Y)
elif tmp == 3:
    print(Y + 3)
