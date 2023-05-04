import itertools

INF = 10 ** 10
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
XY = []
kazu = [i for i in range(N)]


for i in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    XY.append((x, y))

ans = INF
for i in itertools.permutations(kazu, N):
    tmp = 0
    for j in range(N):
        tmp += A[j][i[j]]

    for j in XY:
        if abs(i[j[0]] - i[j[1]]) == 1:
            tmp = INF
            break
    ans = min(ans, tmp)
if ans == INF:
    ans = -1
print(ans)
