N, T = map(int, input().split())
aLst = list(int(input()) for i in range(N))
ans = 0
for i in range(N - 1):
    ans += min(T, aLst[i + 1] - aLst[i])
print(ans + T)
