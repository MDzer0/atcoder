N = int(input())
W = list(map(int, input().split()))

ans = 101
tmp1L = [0] * N
tmp2L = [0] * N
tmp1L[0] = W[0]
tmp2L[N - 1] = W[N - 1]
for i in range(N - 1):
    tmp = 0
    for j in range(0, i + 1):
        tmp += W[j]
    tmp1L[i] = tmp

for i in range(1, N):
    tmp = 0
    for j in range(1, i + 1):
        tmp += W[-j]
    tmp2L[-i] = tmp

for i in range(N - 1):
    ans = min(ans, abs(tmp1L[i] - tmp2L[i + 1]))
print(ans)
