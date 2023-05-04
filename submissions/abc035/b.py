S = input()
T = int(input())

ansLst = [0] * 2
tmp = 0
for i in range(len(S)):
    if S[i] == 'L':
        ansLst[0] -= 1
    elif S[i] == 'R':
        ansLst[0] += 1
    elif S[i] == 'U':
        ansLst[1] += 1
    elif S[i] == 'D':
        ansLst[1] -= 1
    else:
        tmp += 1

if T == 1:
    ans = abs(ansLst[0]) + abs(ansLst[1]) + tmp
else:
    ans = max((tmp - abs(ansLst[0]) -abs(ansLst[1])) % 2, abs(ansLst[0]) + abs(ansLst[1]) - tmp)
print(ans)
