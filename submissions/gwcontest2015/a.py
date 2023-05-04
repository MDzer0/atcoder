tokuten = [25, 39, 51, 76, 163, 111, 128, 133, 138]
gtokuten = [58, 136]
patern = []

for i in range(2 ** 9):
    total = 0
    for j in range(9):
        if i >> j & 1:
            total += tokuten[j]
    patern.append(total)

ans = patern[:]

for i in range(2):
    for j in range(len(patern)):
        ans.append(patern[j] + gtokuten[i])

ans.sort()
ans = set(ans)
for i in ans:
    print(i)
