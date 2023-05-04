N = int(input())
K = int(input())
X = int(input())
Y = int(input())

ans = K * X
if N > K:
    ans += (N - K) * Y
elif N < K:
    ans = ans - ((K - N) * X)
print(ans)
