N, K = map(int, input().split())
A = list(map(int, input().split()))
if K >= N:
    print(*[0] * N)
else:
    print(*(A[K:] + [0] * (K)))
