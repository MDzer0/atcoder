a, b = map(int, input().split())
ans = 0
if a <= b:
    ans = a
else:
    ans = a - 1

print(ans)
