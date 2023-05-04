a, b, c = map(int, input().split())

ab = b - a
bc = c - b

if ab == bc:
    print('YES')
else:
    print('NO')
