N = int(input())
A = list(map(int, input().split()))
A.sort()
for i in range(N):
    A[i] = 2 * A[i] + 1
ans = A[0]

for i in range(1, N):
    ans += A[i] - (A[i - 1] // 2)
print(ans)
