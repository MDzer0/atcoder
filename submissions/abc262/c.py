N = int(input())
A = list(map(int, input().split()))

cnt = 0
for i in range(N):
    if A[i] == i + 1:
        cnt += 1
ans = (cnt * (cnt - 1)) // 2

for i in range(N):
    if i < A[i] - 1 and A[A[i] - 1] - 1== i:
        ans += 1
print(ans)
