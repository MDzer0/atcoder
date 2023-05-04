S = input()

cnt1 = 0
tmp1 = 'I'

for i in S:
    if cnt1 % 2 == 0 and tmp1 == i:
        cnt1 += 1
        tmp1 = 'O'
    elif cnt1 % 2 == 1 and tmp1 == i:
        cnt1 += 1
        tmp1 = 'I'

if tmp1 == 'I':
    cnt1 -= 1

if cnt1 == 2:
    cnt1 = 1
elif cnt1 < 0:
    cnt1 = 0
print(cnt1)
