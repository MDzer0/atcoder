import itertools

N, K = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(N)]
ch = [i for i in range(K)]
anslst = [0] * N
ans = 'Nothing'

def dfs(v):
    global ans
    if v == N:
        tmp = anslst[0]
        for i in range(1, N):
            tmp ^= anslst[i]
        if tmp == 0:
            ans = 'Found'
        return

    for i in range(K):
        anslst[v] = t[v][ch[i]]
        dfs(v + 1)

    return

dfs(0)
print(ans)
