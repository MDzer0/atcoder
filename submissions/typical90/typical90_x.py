N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cnt = 0

for i in range(N):
    cnt += abs(A[i] - B[i])

K -= cnt
if K < 0 or K % 2 == 1:
    print('No')
else:
    print('Yes')
