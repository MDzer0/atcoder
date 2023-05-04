sx, sy, gx, gy = map(int, input().split())
x = gx - sx
y = -gy - sy
tmp = y / x
ans = sy / tmp
print(sx - ans)
