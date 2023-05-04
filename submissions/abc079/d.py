from scipy.sparse.csgraph import floyd_warshall
H, W = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]
a = [list(map(int, input().split())) for _ in range(H)]

wf = floyd_warshall(c)
ans = 0
for i in range(H):
    for j in range(W):
        if a[i][j] == -1 or a[i][j] == 1:
            continue
        else:
            ans += wf[a[i][j]][1]

print(int(ans))
