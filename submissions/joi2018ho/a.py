N, K = map(int, input().split())
a = [int(input()) for _ in range(N)]
rui = [0] * (N - 1)

for i in range(N - 1):
    rui[i] = a[i + 1] - a[i]
rui.append(1)
rui.sort(reverse=True)
print(sum(rui[K - 1:]) + K - 1)
