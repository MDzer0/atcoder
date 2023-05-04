N, K = map(int, input().split())
a = list(map(int, input().split()))
rui = [0] * (N + 1)

for i in range(N):
    rui[i + 1] = rui[i] + a[i]

for i in range(K, N):
    if rui[i] - rui[i - K] < rui[i + 1] - rui[i - K + 1]:
        print('Yes')
    else:
        print('No')
