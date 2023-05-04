N = input()
ans = 10 ** 10
for i in range(1 << len(N)):
    cnt = 0
    tmp = ''
    for j in range(len(N)):
        if i >> j & 1:
            tmp += N[j]
        else:
            cnt += 1
    if tmp != '' and int(tmp) % 3 == 0:
        ans = min(ans, cnt)

print(ans if ans != 10 ** 10 else -1)
