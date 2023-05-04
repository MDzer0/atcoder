S = input()
lenS = len(S)
rui = [0] * 2019
rui[0] = 1
tmp = 1
m = 0
for i in range(lenS):
    m += int(S[-i - 1]) * tmp
    m %= 2019
    tmp *= 10
    tmp %= 2019
    rui[m] += 1

ans = 0
for i in rui:
    if i >= 2:
        ans += (i * (i - 1) // 2)

print(ans)
