N = int(input())
m = list(map(int, input().split()))
ans = 0
for i in m:
    if i < 80:
        ans += 80 - i

print(ans)
