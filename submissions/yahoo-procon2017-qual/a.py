S = input()
ycnt = S.count('y')
acnt = S.count('a')
hcnt = S.count('h')
ocnt = S.count('o')
if ycnt == 1 and acnt == 1 and hcnt == 1 and ocnt == 2:
    print('YES')
else:
    print('NO')
