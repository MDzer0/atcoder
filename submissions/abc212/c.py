import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B.sort()

ans = 10 ** 10

for i in range(N):
    index = bisect.bisect_left(B, A[i])
    if index > 0:
        ans = min(ans ,abs(B[index - 1] - A[i]))
    if index < M:
        ans = min(ans, abs(B[index] - A[i]))

print(ans)
