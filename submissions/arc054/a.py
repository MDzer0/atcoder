L, X, Y, S, D = map(int, input().split())

if S == D:
    print(0)
    exit()

k1 = 0

if S < D:
    k1 = D - S
else:
    k1 = (L - S) + D

k2 = L - k1
tmp1 = k1 / (X + Y)

if X == Y:
    print(tmp1)
    exit()
    
tmp2 = k2 / (Y - X)
ans = 0
if tmp2 <= 0:
    ans = tmp1
else:
    ans = min(tmp1, tmp2)

print(ans)
