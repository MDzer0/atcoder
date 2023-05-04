N, M, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
arui = [0] * (N + 1)
brui = [0] * (M + 1)
for i in range(N):
    arui[i + 1] = a[i] + arui[i]
for i in range(M):
    brui[i + 1] = b[i] + brui[i]

ans = 0
bcnt = M
for i in range(N + 1):
    if arui[i] > K:
        break

    while brui[bcnt] + arui[i] > K:
        bcnt -= 1
    ans = max(ans, i + bcnt)

print(ans)
