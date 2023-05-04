import string
S = input()
ans = ''
if len(S) != 26:
    for i in string.ascii_lowercase:
        if S.count(i) == 0:
            ans = S + i
            break
else:
    tmp = []
    tmp.append(S[-1])
    loopF = False
    for i in range(len(S) - 2, -1, -1):
        for j in range(len(tmp)):
            if S[i] < tmp[j]:
                ans = S[0:i] + tmp[j]
                loopF = True
                break

            if j == len(tmp) - 1:
                tmp.append(S[i])
                tmp.sort()
        if loopF:
            break
if ans == '':
    print(-1)
else:
    print(ans)
