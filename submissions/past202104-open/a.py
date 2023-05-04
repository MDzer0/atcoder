S = input()
cntflg = False
for i in range(len(S)):
    if i == 3 and S[i] == '-':
        cntflg = True
        continue
    if not(S[i].isdigit()):
        print('No')
        exit()

if cntflg:
    print('Yes')
else:
    print('No')
