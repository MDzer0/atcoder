X, t = map(int, input().split())

ans = X - t
if ans < 0:
    print(0)
else:
    print(ans)
