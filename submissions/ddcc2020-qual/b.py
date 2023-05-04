import statistics
N = int(input())
A = list(map(int, input().split()))
tmp1 = [0] * N
tmp2 = [0] * N
tmp1[0] = A[0]
tmp2[-1] = A[-1]
for i in range(1, N):
    tmp1[i] = abs(tmp1[i - 1] + A[i])
    tmp2[-i - 1] = abs(tmp2[-i] + A[-i - 1])
ans = 10 ** 10
for i in range(N - 1):
    ans = min(ans, abs(tmp1[i] - tmp2[i + 1]))
print(ans)
