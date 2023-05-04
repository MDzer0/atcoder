import math
H, W = map(int, input().split())

if H == 1 or W == 1:
    print(1)
    exit()
    
ans = math.ceil(H / 2) * math.ceil(W / 2)
ans += (H // 2) * (W // 2)

print(ans)
