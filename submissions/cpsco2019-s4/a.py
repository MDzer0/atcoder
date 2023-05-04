L, X = map(int, input().split())
v, m = divmod(X, L)
if v % 2 != 0:
    print(L - m)
else:
    print(m)
