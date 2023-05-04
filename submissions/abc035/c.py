N, Q = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(Q)]

imos = [0] * (N + 1)
for i in range(Q):
    imos[lr[i][0] - 1] += 1
    imos[lr[i][1]] -= 1
ans = []
for i in range(1, N + 1):
    tmp = imos[i - 1] + imos[i]
    imos[i] = tmp
    ans.append(imos[i - 1] % 2)

anslst = [str(i) for i in ans]
print(''.join(anslst))
