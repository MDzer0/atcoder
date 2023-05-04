H, W = map(int, input().split())
ans = 0
if W > 1:
    ans += (W - 1) * H

if H > 1:
    ans += (H - 1) * W

print(ans)
