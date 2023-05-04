N, M = map(int, input().split())
X = list(map(int, input().split()))
t = sorted(X, reverse=True)
h = [0] * M
for i in range(1, M):
    h[i] = abs(t[i - 1] - t[i])

tmp = sorted(h, reverse=True)
print(sum(tmp[N - 1:]))
