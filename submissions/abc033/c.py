S = input()
tmp = S.split('+')
acnt = 0
for i in tmp:
    v = i.split('*')
    cntf = True
    for j in v:
        if j == '0':
            cntf = False
            break
    if cntf:
        acnt += 1

print(acnt)
