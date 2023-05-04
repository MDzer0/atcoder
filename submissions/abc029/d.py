N = int(input())
ans = 0
kake = 1
waru = 10
for i in range(1, len(str(N)) + 1):
    tmp = (N + 1) // waru ** i
    m = (N + 1) % waru ** i
    add = 0
    if m >= waru ** (i - 1):
        add = min(m, 2 * (kake * 10 ** (i - 1))) - kake * 10 ** (i - 1)
    ans += (tmp * kake * 10 ** (i - 1)) + add

print(ans)
