N, A = map(int, input().split())
mincnt = 0
if A != 0:
    mincnt = A // 3 if A % 3 == 0 else (A // 3) + 1
print(mincnt, min(N // 3, A))
