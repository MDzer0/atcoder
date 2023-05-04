S = input()
T = input()
ansCnt = 0
for i in range(len(S)):
    if S == T:
        break
    S = S[-1] + S[0:-1]
if S == T:
    print('Yes')
else:
    print('No')
