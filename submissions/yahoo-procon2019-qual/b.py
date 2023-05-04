miti = [0, 0, 0, 0]
d = [[] for _ in range(4)]

for i in range(3):
    a, b = map(int, input().split())
    d[a - 1].append(b - 1)
    d[b - 1].append(a - 1)

miti[0] = 1
index = 0
for i in range(3):
    for j in range(len(d[index])):
        if j < len(d[index]) and miti[d[index][j]] != 1:
            miti[d[index][j]] = 1
            index = d[index][j]

if sum(miti) == 4:
    print('YES')
else:
    print('NO')
