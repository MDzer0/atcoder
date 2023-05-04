n, a, b = map(int, input().split())
cnt = n - a - b
if cnt < 0:
    print(abs(cnt))
else:
    print(0)
