H, W, D = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(H)]
rui = [0] * (H * W)
indexLst = [[0, 0] for _ in range(H * W)]
for i in range(H):
    for j in range(W):
        indexLst[a[i][j] - 1] = [i + 1, j + 1]

for i in range(D, H * W):
    rui[i] += abs(indexLst[i][0] - indexLst[i - D][0]) + abs(indexLst[i][1] - indexLst[i - D][1]) + rui[i - D]

Q = int(input())
for i in range(Q):
    L, R = map(int, input().split())
    print(rui[R - 1] - rui[L - 1])
