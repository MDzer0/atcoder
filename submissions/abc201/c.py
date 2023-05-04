S = input()
must = []
koho = []

for i in range(len(S)):
    if S[i] == 'o':
        must.append(str(i))
        koho.append(str(i))
    elif S[i] == '?':
        koho.append(str(i))

cnt = 0
for i in koho:
    for j in koho:
        for k in koho:
            for l in koho:
                tmp = i + j + k + l
                cflg = True
                for m in must:
                    if not m in tmp:
                        cflg = False
                if cflg:
                    cnt += 1

print(cnt)
