W, H, x, y = map(int, input().split())

ans = (W * H) / 2
anscnt = 0

if W - x == x and H - y == y:
    anscnt = 1
    
print(ans, end=' ')
print(anscnt)
