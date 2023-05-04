X, Y, A, B = map(int, input().split())

tmp1 = X * A
tmp2 = X + B
ans = 1
if tmp1 >= tmp2:
    m, d = divmod(Y - tmp2, B)
    ans += m
    if d == 0:
        ans -= 1
    print(ans)
    exit()

while tmp2 > tmp1:
    if tmp1 >= Y:
        print(ans - 1)
        exit()
    tmp2 = tmp1 + B
    tmp1 *= A
    if min(tmp1, tmp2) < Y:
        ans += 1
    else:
        print(ans)
        exit()

if tmp2 >= Y:
    print(ans)
else:
    m, d = divmod(Y - tmp2, B)
    ans += m
    if d == 0:
        ans -= 1
    print(ans)

