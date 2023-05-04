M, N = map(int, input().split())
m, d = divmod(M, N)

if d == 0:
    print(m)
else:
    print(M // N + d)
