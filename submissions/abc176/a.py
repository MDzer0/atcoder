N, X, T = map(int, input().split())
m,d = divmod(N, X)
if d != 0:
    m += 1
print(m * T)
