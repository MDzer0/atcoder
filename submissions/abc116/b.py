def kansu(s):
    if s % 2 == 0:
        s = s / 2
    else:
        s = 3 * s + 1
    return s

s = int(input())
ansFlg = True

if s == 4 or s == 1 or s == 2:
    print(4)
    exit()

ans = 1
while ansFlg:
    if s == 4:
        ans += 3
        break
    s = kansu(s)
    ans += 1
print(ans)
