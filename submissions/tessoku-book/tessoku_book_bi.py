N, M = map(int, input().split())
g = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    g[a - 1].append(b)
    g[b - 1].append(a)

for i in range(N):
    print(i + 1, end='')
    print(': {', end='')
    print(*g[i], sep=', ', end='')
    print('}', end='\n')
