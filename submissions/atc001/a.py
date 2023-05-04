def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def same(x, y):
    if find(x) == find(y):
        return True
    else:
        return False

def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

N, Q = map(int, input().split())
par = [i for i in range(N)]
rank = [0] * N
for i in range(Q):
    p, a, b = map(int, input().split())
    if p == 0:
        unite(a, b)
    else:
        if same(a, b):
            print('Yes')
        else:
            print('No')
