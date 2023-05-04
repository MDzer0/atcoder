import sys
S = input()
T = input()
ans = 'UNRESTORABLE'

tmp = True
anss = -1
anse = -1
for i in range(len(S) - len(T) + 1):
    tmp = True
    s = i
    e = i + len(T)
    for j in range(len(T)):
        if S[i + j] != '?' and\
            S[i + j] != T[j]:
            tmp = False
            break

    if tmp:
        anss = i
        anse = i + len(T)

if anss == -1:
    print(ans)

else:
    ans = S.replace('?', 'a')
    ans = ans[:anss] + T + ans[anse:]
    print(ans)
