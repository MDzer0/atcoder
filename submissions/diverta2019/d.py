def yakusu(n):
    defyaku = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            defyaku.append(i)
            if i != n // i:
                defyaku.append(n // i)
    return defyaku

N = int(input())
yaku = yakusu(N)
ans = 0
for i in yaku:
    if i == 1: continue
    v, n = divmod(N, i - 1)
    if v == n:
        ans += (i - 1)

print(ans)
