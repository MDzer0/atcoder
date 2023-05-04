N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
X = int(input())
dp = [0] * (X + 1)
dp[0] = 1
for i in B:
    dp[i] = 2

for i in range(X + 1):
    for j in range(N):
        if i - A[j] >= 0:
            if dp[i - A[j]] == 1 and dp[i] != 2:
                dp[i] = 1
if dp[X] == 1:
    print('Yes')
else:
    print('No')
