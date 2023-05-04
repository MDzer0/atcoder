class SegmentTree:
    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.dat = [0] * (self.size * 2)

    def update(self, pos, x):
        pos += self.size
        self.dat[pos] = x
        while pos >= 2:
            pos //= 2
            self.dat[pos] = self.dat[pos * 2] + self.dat[pos * 2 + 1]

    def query(self, l, r, a, b, u):
        if r <= a or b <= l: return 0
        if l <= a and b <= r: return self.dat[u]
        m = (a + b) // 2
        ansl = self.query(l, r, a, m, u * 2)
        ansr = self.query(l, r, m, b, u * 2 + 1)
        return ansl + ansr

N = int(input())
A = list(map(int, input().split()))
t = SegmentTree(N)

ans = 0
for i in A:
    ans += t.query(i, N, 0, t.size, 1)
    t.update(i - 1, 1)
print(ans)
