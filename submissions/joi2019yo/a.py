A, B, C = map(int, input().split())
ans = 0
total = A * 7 + B
m, d = divmod(C, total)
if m == 0:
    if C > 6 * A:
        print(7)
        exit()
    else:
        m, d = divmod(C, A)
        if d == 0:
            print(m)
            exit()
        else:
            print(m + 1)
            exit()
ans += m * 7
m, d = divmod(d, A)
if m >= 7:
    print(ans + 7)
elif d == 0:
    print(ans + m)
else:
    print(ans + m + 1)
