import string
S = input()
tmp = S[0]
anslst = []

for i in S[1:]:
    if string.ascii_lowercase.count(i) == 1:
        tmp += i
    else:
        if tmp == '':
            tmp += i
        else:
            tmp += i
            anslst.append(tmp)
            tmp = ''

anslst.sort(key=str.lower)
print(''.join(anslst))
