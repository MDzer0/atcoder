import sys
sys.setrecursionlimit(10**6)
def dfs(y):
    global asum
    global bsum
    chklist[y] = -1
    for i in ki[y]:
        if chklist[i] == -1:
            continue
        asum += a[i]
        bsum += b[i]
        dfs(i)
    return

N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
chklist = [0] * N

ki = [[] for _ in range(N)]
for i in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    ki[x].append(y)
    ki[y].append(x)

for i in range(N):
    if chklist[i] == -1:
        continue
    asum = a[i]
    bsum = b[i]
    dfs(i)
    if asum != bsum:
        print('No')
        exit()
print('Yes')
