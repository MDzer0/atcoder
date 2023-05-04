INF = 10 ** 18

N = int(input())
B = list(map(int, input().split()))
A = [INF] * N
A[0] = B[0]

for i in range(1, N - 1):
    A[i] = min(B[i - 1], B[i])
A[-1] = B[-1]
print(sum(A))
