N = int(input())
ans = 0
for i in range(N):
    a, b = map(int, input().split())
    ans += max(a, b)
print(ans)
