N, A, B = map(int, input().split())
minn = A * (N - 1) + B
maxn = B * (N - 1) + A
if minn > maxn:
    print(0)
elif minn == maxn:
    print(1)
else:
    print(maxn - minn + 1)
