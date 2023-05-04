H, W = map(int, input().split())
HWList = [[0] * (W + 1) for _ in range(H + 1)]
for i in range(1, H + 1):
    tmp = list(map(int, input().split()))
    for j in range(W):
        HWList[i][j + 1] = tmp[j]

for i in range(1, H + 1):
    for j in range(W):
        HWList[i][j + 1] += HWList[i][j]
for i in range(1, W + 1):
    for j in range(H):
        HWList[j + 1][i] += HWList[j][i]

Q = int(input())
for i in range(Q):
    A, B, C, D = map(int, input().split())
    ans = HWList[A - 1][B - 1] + HWList[C][D]\
          - HWList[C][B - 1] - HWList[A - 1][D]
    print(ans)
