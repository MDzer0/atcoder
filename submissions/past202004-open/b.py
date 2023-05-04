S = input()

acnt = S.count('a')
bcnt = S.count('b')
ccnt = S.count('c')

if acnt > bcnt and acnt > ccnt:
    print('a')
elif bcnt > acnt and bcnt > ccnt:
    print('b')
else:
    print('c')
