N, T, E = map(int, input().split())
x = list(map(int, input().split()))

for i in range(N):
    tmp1 = T // x[i] * x[i]
    tmp2 = tmp1 + x[i]
    if T - E <= tmp1 <= T + E\
        or T - E <= tmp2 <= T + E:
        print(i + 1)
        exit()
print(-1)
