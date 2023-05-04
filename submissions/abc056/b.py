W, a, b = map(int, input().split())
ans = 0
if a < b and (a + W) < b:
    ans = abs((a + W) - b)
elif a > b and (b + W) < a:
    ans = abs((b + W) - a)

print(ans)
