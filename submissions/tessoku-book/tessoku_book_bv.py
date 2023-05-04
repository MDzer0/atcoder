N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]
X = [-1] * N
Y = [-1] * N

for i in range(N):
    for j in range(N):
        if P[i][j] != 0:
            X[i] = P[i][j]
            Y[j] = P[i][j]
cntX = 0
cntY = 0
for i in range(N):
    for j in range(i + 1, N):
        if X[i] > X[j]: cntX += 1
        if Y[i] > Y[j]: cntY += 1

print(cntX + cntY)
