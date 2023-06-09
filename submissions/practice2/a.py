def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
# 同一の集合の判定
def same(x, y):
    if find(x) == find(y):
        return True
    else:
        return False
# 集合の併合
def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if par[x] > par[y]:
        x, y = y, x
    par[x] += par[y]
    par[y] = x

# 集合の数
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
