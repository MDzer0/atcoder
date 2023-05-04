import string
S = input()
slst = list(string.ascii_lowercase + '.')

cnt = 0
if len(S) >= 3:
    for i in slst:
        for j in slst:
            for k in slst:
                for l in range(len(S) - 2):
                    if (i == S[l] or i == '.') and (j == S[l + 1] or j == '.')\
                            and (k == S[l + 2] or k == '.'):
                        cnt += 1
                        break

if len(S) >= 2:
    for i in slst:
        for j in slst:
            for l in range(len(S) - 1):
                if (i == S[l] or i == '.') and (j == S[l + 1] or j == '.'):
                    cnt += 1
                    break

if len(S) >= 1:
    for i in slst:
        if i == '.' or S.count(i) > 0:
            cnt += 1

print(cnt)
