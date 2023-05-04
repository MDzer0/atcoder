X, K, D = map(int, input().split())
scnt = abs(X) // D
if K <= scnt:
    print(abs(X) - K * D)
else:
    if X % D == 0:
        if (K - scnt) % 2 == 0:
            print(0)
        else:
            print(D)
    else:
        if (K - scnt) % 2 == 0:
            print(abs(abs(X) - scnt * D))
        else:
            print(abs(abs(X) - (scnt + 1) * D))
