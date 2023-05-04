abc = list(map(int, input().split()))
ans = 0
for i in abc:
    ans += (7 - i)

print(ans)
