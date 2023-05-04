X, Y, N = map(int, input().split())
print(min(X * N, (N // 3) * Y + (N % 3) * X))
