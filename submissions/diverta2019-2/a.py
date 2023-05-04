M, N = map(int, input().split())
ans = 0
if N == 1:
    ans = 0
else:
    ans = M - N
print(ans)
