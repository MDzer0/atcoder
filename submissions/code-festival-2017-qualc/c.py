s = input()
findex = 0
eindex = len(s) - 1
cnt = 0
ftmp = 0
if len(s) == 1:
    print(0)
    exit()
while eindex - findex > 0:

    if s[findex] == s[eindex]:
        findex += 1
        eindex -= 1
        continue

    else:
        if s[eindex] != 'x' and s[findex] == 'x':
            findex += 1
            cnt += 1
        elif s[findex] != 'x' and s[eindex] == 'x':
            eindex -= 1
            cnt += 1
        else:
            cnt = -1
            break

print(cnt)
