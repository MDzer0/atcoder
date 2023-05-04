N, S = input().split()
ans = 0

for i in range(int(N)):
    atcnt = 0
    cgcnt = 0
    for j in range(i, int(N)):
        if S[j] == 'A':
            atcnt += 1
        elif S[j] == 'T':
            atcnt -= 1
        elif S[j] == 'C':
            cgcnt += 1
        else:
            cgcnt -= 1

        if atcnt == 0 and cgcnt == 0:
            ans += 1

print(ans)
