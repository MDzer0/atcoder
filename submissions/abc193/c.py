N = int(input())
haijo = []
if N == 1:
    print(1)
    exit()

for i in range(2, int(N ** 0.5) + 1):
    tmp = i * i
    while N >= tmp:
        haijo.append(tmp)
        tmp *= i

haijo = set(haijo)
print(N - len(haijo))
