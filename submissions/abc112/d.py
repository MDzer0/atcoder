N, M = map(int, input().split())
tmp = M // N
ansMax = 0
y = []
for i in range(1, (int(M ** (0.5)) + 1)):
    if M % i == 0:
        y.append(i)
        if i != M // i:
            y.append(M // i)
y.sort()

for i in y:
    if i <= tmp:
        ansMax = i
    else:
        break
print(ansMax)
