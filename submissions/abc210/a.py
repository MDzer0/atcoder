N, A, X, Y = map(int, input().split())
if N <= A:
    print(X * N)
else:
    print((X * A) + (N - A) * Y)
