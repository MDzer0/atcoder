x1, y1, x2, y2, x3, y3 = map(int, input().split())

ans = abs(((x1 - x3) * (y2 - y3)) - ((x2 - x3) * (y1 - y3)))
ans = ans / 2
print(ans)
