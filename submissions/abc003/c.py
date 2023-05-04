N, K = map(int, input().split())
r = list(map(int, input().split()))
r.sort()

ans = 0
for i in range(K, 0, -1):
    ans = (ans + r[-i]) / 2

print(ans)
