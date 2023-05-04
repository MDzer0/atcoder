a, b, c = map(int, input().split())
d = 0
ans = 3
if a == b:
    d += 1

if a == c:
    d += 1

if b == c:
    d += 1
if d == 3:
    d = 2

print(ans - d)
