M, N = map(int, input().split())
ans = 0
for i in range(M):
    a = list(map(int, input().split()))
    ans = max(ans, a.count(1))

print(ans)
