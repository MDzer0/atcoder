N = int(input())
ans = 0
for i in range(N):
    i, j = map(int, input().split())
    ans += j - i + 1

print(ans)
