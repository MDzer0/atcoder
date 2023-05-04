H, W, N = map(int, input().split())
HW = [[0] * (W + 2) for _ in range(H + 2)]
for i in range(N):
    A, B, C, D = map(int, input().split())
    HW[A][B] += 1
    HW[C + 1][B] -= 1
    HW[C + 1][D + 1] += 1
    HW[A][D + 1] -= 1

for i in range(1, H + 1):
    for j in range(W + 1):
        HW[i][j + 1] += HW[i][j]

for i in range(1, W + 1):
    for j in range(H + 1):
        HW[j + 1][i] += HW[j][i]

for i in range(1, H + 1):
    print(*HW[i][1:W + 1])
