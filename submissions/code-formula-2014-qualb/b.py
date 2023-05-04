N = input()
k = 0
g = 0
for i in range(len(N)):
    if i % 2 == 0:
        k += int(N[-i - 1])
    else:
        g += int(N[-i - 1])

print(g, k)
