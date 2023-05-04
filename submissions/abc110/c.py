import string
import sys
S = input()
T = input()
sLst = [0] * 26
tLst = [0] * 26

for i in range(26):
    sLst[i] = S.count(string.ascii_lowercase[i])
    tLst[i] = T.count(string.ascii_lowercase[i])
sLst.sort(reverse=True)
tLst.sort(reverse=True)

for i in range(26):
    if sLst[i] != tLst[i]:
        print('No')
        sys.exit()

print('Yes')
