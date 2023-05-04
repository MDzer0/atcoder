N = int(input())
ab = []
MOD = 10 ** 9 + 7
ans = 1

for i in range(2 * N):
    if i < N:
        ab.append([int(input()), 'a'])
    else:
        ab.append([int(input()), 'b'])

ab.sort(key=lambda x: x[0])
cnt = 0
for v, tmp in ab:
    if tmp == 'a':
        if cnt < 0:
            ans *= abs(cnt)
        cnt += 1
    else:
        if cnt > 0:
            ans *= cnt
        cnt -= 1
    ans %= MOD

print(ans)
