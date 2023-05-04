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

N, Q = map(int, input().split())
par = [-1 for i in range(N)]

for i in range(Q):
    tmp = list(map(int, input().split()))
    if tmp[0] == 0:
        unite(tmp[1], tmp[2])
    else:
        if same(tmp[1], tmp[2]):
            print(1)
        else:
            print(0)
