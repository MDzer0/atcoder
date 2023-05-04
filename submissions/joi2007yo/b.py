seito = [0] * 31
for i in range(28):
    index = int(input())
    seito[index] = 1

for i in range(1, 31):
    if seito[i] == 0:
        print(i)
