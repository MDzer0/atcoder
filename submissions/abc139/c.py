N = int(input())
h = list(map(int, input().split()))

ans = 0
atmp = 0

for i in range(1, N):
    if h[i - 1] >= h[i]:
        atmp += 1
    else:
        ans = max(ans, atmp)
        atmp = 0
ans = max(ans, atmp)

print(ans)
