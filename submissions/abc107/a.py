N, i = map(int, input().split())
ans = 0
if N == 1:
    ans = 1
else:
    ans = N - i + 1
print(ans)
