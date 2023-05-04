N, M = map(int, input().split())
HATA = [input() for _ in range(N)]

Wcnt = 0
ans = 10 ** 19
for i in range(N - 2):
    Wcnt += M - HATA[i].count('W')
    Bcnt = 0
    for j in range(i + 1, N - 1):
        Bcnt += M - HATA[j].count('B')
        Rcnt = 0
        for k in range(j + 1, N):
            Rcnt += M - HATA[k].count('R')
        ans = min(ans, Wcnt + Bcnt + Rcnt)

print(ans)
