H, W = map(int, input().split())
ans = 0
if H == 1 or W == 1:
    print(H * W)
    exit()
for i in range(0, H, 2):
    for j in range(0, W, 2):
        ans += 1

print(ans)
