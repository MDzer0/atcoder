s = input()
minc = 101
maxf = 0

for i in range(len(s)):
    if minc == 101:
        if s[i] == 'C':
            minc = i

    if maxf == 0:
        if s[-i - 1] == 'F':
            maxf = len(s) - i - 1

if minc < maxf:
    print('Yes')
else:
    print('No')
