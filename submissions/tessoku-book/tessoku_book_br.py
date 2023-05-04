from collections import deque

def nextPost(pos, x, y, z):
    state = [(pos // (2 ** i)) % 2 for i in range(N)]
    state[x] = 1 - state[x]
    state[y] = 1 - state[y]
    state[z] = 1 - state[z]

    ret = 0
    for i in range(N):
        if state[i] == 1:
            ret += 2 ** i
    return ret

N, M = map(int, input().split())
A = list(map(int, input().split()))
XYZ = [list(map(int, input().split())) for _ in range(M)]
G = [[] for _ in range(2 ** N)]
for i in range(2 ** N):
    for x, y, z in XYZ:
        next = nextPost(i, x - 1, y - 1, z - 1)
        G[i].append(next)

start = 0
for i in range(N):
    if A[i] == 1:
        start += 2 ** i
goal = 2 ** N - 1
dist = [-1 for _ in range(2 ** N)]
dist[start] = 0
que = deque()
que.append(start)

while que:
    pos = que.popleft()
    for i in G[pos]:
        if dist[i] == -1:
            dist[i] = dist[pos] + 1
            que.append(i)

print(dist[goal])
