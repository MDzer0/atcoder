import sys
sys.setrecursionlimit(10**6)

def dfs(index):
    if toshiF[index] == 1: return
    toshiF[index] = 1
    for i in toshi[index]:
        dfs(i)
    return

N, M = map(int, input().split())
toshi = [[] for _ in range(N)]


for i in range(M):
    a, b = map(int, input().split())
    toshi[a - 1].append(b - 1)

ans = 0
for i in range(N):
    cnt = 0
    toshiF = [0] * N
    dfs(i)
    ans += sum(toshiF)

print(ans)
