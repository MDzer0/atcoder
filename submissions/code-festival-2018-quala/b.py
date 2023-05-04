N, M, A, B = map(int, input().split())
mikan = [0] * N
for i in range(M):
    l, r = map(int, input().split())
    for j in range(l - 1, r):
        if mikan[j] == 1: continue
        mikan[j] = 1

ans = 0
for i in mikan:
    if i == 1:
        ans += A
    else:
        ans += B
print(ans)
