from collections import deque

N, M = map(int, input().split())
g = [[] for _ in range(N)]
ki = [-1] * N
for i in range(M):
    A, B = map(int, input().split())
    g[A - 1].append(B - 1)
    g[B - 1].append(A - 1)

que = deque()
que.append((0, 0))
ki[0] = 0
while que:
    tmp = que.popleft()
    for i in g[tmp[0]]:
        if ki[i] == -1:
            ki[i] = tmp[1] + 1
            que.append((i, tmp[1] + 1))
for i in ki:
    print(i)
