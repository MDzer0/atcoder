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
    a, b = map(int, input().split())
    unite(a - 1, b - 1)

ans = set()
for i in range(N):
    ans.add(find(i))
print(len(ans) - 1)
