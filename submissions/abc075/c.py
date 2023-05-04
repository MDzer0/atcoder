import copy

class UNION:
    def __init__(self):
        return
    def find(self, x):
        if par[x] < 0:
            return x
        else:
            par[x] = self.find(par[x])
            return par[x]

    # “¯ˆê‚ÌW‡‚Ì”»’è
    def same(self, x, y):
        if self.self.find(x) == self.find(y):
            return True
        else:
            return False
    # W‡‚Ì•¹‡
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if par[x] > par[y]:
            x, y = y, x
        par[x] += par[y]
        par[y] = x

# W‡‚Ì”
def uCnt(self,x):
    return -par[self.find(x)]

N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]
cpar = [-1 for i in range(N)]
jiko = []
for i in range(M):
    par = copy.deepcopy(cpar)
    u = UNION()
    for j in range(M):
        if j == i:continue
        a = ab[j][0] - 1
        b = ab[j][1] - 1
        u.unite(a, b)
    tmp = min(par)
    if tmp == -N:
        jiko.append(i)

par = copy.deepcopy(cpar)
u = UNION()
for i in range(M):
    if jiko.count(i) == 0:
        a = ab[i][0] - 1
        b = ab[i][1] - 1
        u.unite(a, b)
ans = 0
for i in par:
    if i < -1:
        ans += abs(i) - 1

print(ans)
