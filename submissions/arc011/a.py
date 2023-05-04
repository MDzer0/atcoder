m, n, N = map(int, input().split())
cnt = N
tmp = N
amari = 0
for i in range(N):
    cnt += (tmp // m) * n
    amari += tmp % m
    tmp = (tmp // m) * n

    if amari >= m:
        cnt += (amari // m) * n
        tmp += (amari // m) * n
        amari = (amari % m)

print(cnt)
