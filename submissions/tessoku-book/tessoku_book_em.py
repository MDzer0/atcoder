class unionfind:
    def __init__(self, n):
        self.n = n
        self.par = [-1] * (n + 1)
        self.size = [1] * (n + 1)

    def root(self, x):
        while self.par[x] != -1:
            x = self.par[x]
        return x

    def unite(self, u, v):
        rootu = self.root(u)
        rootv = self.root(v)
        if rootu != rootv:
            if self.size[rootu] < self.size[rootv]:
                self.par[rootu] = rootv
                self.size[rootv] += self.size[rootu]
            else:
                self.par[rootv] = rootu
                self.size[rootu] += self.size[rootv]

    def same(self, u, v):
        return self.root(u) == self.root(v)

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
Q = int(input())
query = [list(map(int, input().split())) for _ in range(Q)]
last = [True] * (M + 1)
for i in query:
    if i[0] == 1:
        last[i[1]] = False

uf = unionfind(N)
for i in range(1, M + 1):
    if last[i]:
        uf.unite(AB[i - 1][0], AB[i - 1][1])

ans = []
for i in reversed(query):
    if i[0] == 1:
        uf.unite(AB[i[1] - 1][0], AB[i[1] - 1][1])
    else:
        if uf.same(i[1], i[2]):
            ans.append('Yes')
        else:
            ans.append('No')
for i in reversed(ans): print(i)
