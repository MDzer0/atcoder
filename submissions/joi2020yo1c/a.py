X, L, R = map(int, input().split())
tmp = 10 ** 18
ans = 0
for i in range(L, R + 1):
    if abs(X - i) <= tmp:
        tmp = abs(X - i)
        ans = i
print(ans)
