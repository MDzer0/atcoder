N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    tmp = A[i]
    for j in range(i, N):
        tmp = min(tmp, A[j])
        ans = max(ans, tmp * (j - i + 1))

print(ans)
