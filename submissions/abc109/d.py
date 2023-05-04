H, W = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(H)]
anslst = []
cnt = 0
for i in range(H):
    for j in range(W):
        if a[i][j] % 2 == 1:
            if i != H - 1 and j == W - 1:
                cnt += 1
                anslst.append((i + 1, j + 1))
                anslst.append((i + 2, j + 1))
                a[i + 1][j] += 1
            elif j != W - 1:
                cnt += 1
                anslst.append((i + 1, j + 1))
                anslst.append((i + 1, j + 2))
                a[i][j + 1] += 1

print(cnt)
for i in range(0, 2 * cnt, 2):
    print(anslst[i][0], anslst[i][1], anslst[i + 1][0], anslst[i + 1][1])
