N, M, X, T, D = map(int, input().split())
tmp = T - (X * D)
minK = min(X, M)
print(tmp + (D * minK))
