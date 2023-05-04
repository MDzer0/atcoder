N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [0] * N
dp[1] = A[0]
for i in range(2, N):
    dp[i] = min(dp[i - 1] + A[i - 1], dp[i - 2] + B[i - 2])
ans =[]
tmp = N

while True:
    ans.append(tmp)
    if tmp == 1: break
    if dp[tmp - 1] - A[tmp - 2] == dp[tmp - 2]:
        tmp -= 1
    else:
        tmp -=  2
print(len(ans))
print(*reversed(ans))
