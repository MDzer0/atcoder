N, M = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for i in range(1, M + 1):
    tmpcnt = A.count(i)
    ans = max(ans, tmpcnt)
print(ans)
