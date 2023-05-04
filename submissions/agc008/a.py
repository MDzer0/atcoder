x, y = map(int, input().split())
ans = 0
minxy = min(abs(x), abs(y))
maxxy = max(abs(x), abs(y))
tmp = abs(maxxy - minxy)
if x == 0:
    if y < 0:
        ans = tmp + 1
    else:
        ans = tmp
elif y == 0:
    if x < 0:
        ans = tmp
    else:
        ans = tmp + 1

elif x >= 0 and y >= 0:
    if x < y:
        ans = tmp
    else:
        ans = tmp + 2
elif x <= 0 and y <= 0:
    if y < x:
        ans = tmp + 2
    else:
        ans = tmp
else:
    ans = tmp + 1

print(ans)
