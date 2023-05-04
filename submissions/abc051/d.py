from scipy.sparse.csgraph import floyd_warshall

INF = 10 ** 18
N, M = map(int, input().split())
d = [[INF for _ in range(N)] for _ in range(N)]
abc = []

for i in range(M):
    a, b, c = map(int, input().split())
    abc.append([a - 1, b - 1, c])
    d[a - 1][b - 1] = c
    d[b - 1][a - 1] = c

wf = floyd_warshall(d)
cnt = 0
for i in range(M):
    if abc[i][2] > wf[abc[i][0]][abc[i][1]]:
        cnt += 1


print(cnt)
