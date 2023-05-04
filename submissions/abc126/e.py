def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
# “¯ˆê‚ÌW‡‚Ì”»’è
def same(x, y):
    if find(x) == find(y):
        return True
    else:
        return False
# W‡‚Ì•¹‡
def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if par[x] > par[y]:
        x, y = y, x
    par[x] += par[y]
    par[y] = x

# W‡‚Ì”
def uCnt(x):
    return -par[find(x)]


N, M = map(int, input().split())
par = [-1 for i in range(N)]
for i in range(M):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    unite(x, y)

ans = [i for i in range(N) if par[i] < 0]
print(len(ans))
