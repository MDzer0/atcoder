S = input()
wincont = S.count('o')
k = len(S)
sa = 15 - k
wincont = wincont + sa
if wincont >= 8:
    print('YES')
else:
    print('NO')
