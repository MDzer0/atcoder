N = int(input())
S = input()
tmp = S[:(N // 2)]
if S == tmp + tmp:
    print('Yes')
else:
    print('No')
