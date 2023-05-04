N = int(input())
A = list(map(int, input().split()))

ans = 0
maxA = 0
plusA = 0

for i in range(N):
    maxA = max(maxA, A[i])
    plusA += A[i]
    ans += plusA
    print(ans + maxA * (i + 1))
