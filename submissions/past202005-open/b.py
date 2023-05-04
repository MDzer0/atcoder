N, M, Q = map(int, input().split())
mlst = [[0 for _ in range(N)] for _ in range(M)]
tlst = [N] * M
for i in range(Q):
    ilst = list(map(int, input().split()))
    if ilst[0] == 1:
        total = 0
        for j in range(M):
            if mlst[j][ilst[1] - 1] != 0:
                total += tlst[j]
        print(total)
    else:
        tlst[ilst[2] - 1] -= 1
        mlst[ilst[2] - 1][ilst[1] - 1] = tlst[ilst[2] - 1]
