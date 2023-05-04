N = int(input())
s = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0
for i in range(N):
    ans = max(ans, s[i] * a[i])

print(ans)
