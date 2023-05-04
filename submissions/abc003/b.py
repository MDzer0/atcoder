S = input()
T = input()
boolans = True
for i in range(0, len(S)):
    if S[i] != T[i]:
        ans = 'You will lose'
        if S[i] == '@':
            if T[i] not in 'atcoder@':
                boolans = False
                break
            else:
                continue
        elif T[i] == '@':
            if S[i] not in 'atcoder@':
                boolans = False
                break
            else:
                continue
        boolans = False
if boolans:
    print('You can win')
else:
    print('You will lose')
