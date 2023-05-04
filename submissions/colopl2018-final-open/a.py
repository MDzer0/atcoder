N = int(input())
S = input()
if len(S) == 1:
    if S[0] == 'A':
        print(((N + 1) * N) // 2)
    else:
        print(0)
    exit()

acnt = []
cnt = 0
for i in S:
    if i == 'A':
        cnt += 1
    else:
        if cnt != 0:
            acnt.append(cnt)
            cnt = 0

if cnt != 0:
    acnt.append(cnt)
if len(acnt) == 0:
    print(0)
    exit()

ans = 0
for i in range(1, len(acnt) - 1):
    ans += (((acnt[i] + 1) * (acnt[i])) // 2) * N

if len(acnt) == 1:
    if S[-1] == 'A' and S[0] == 'A':
        acnt[0] *= N
        ans += (((acnt[0] + 1) * acnt[0]) // 2)
    else:
        ans += (((acnt[0] + 1) * acnt[0]) // 2) * N
else:
    if S[-1] == 'A':
        ans += (((acnt[0] + acnt[-1] + 1) * (acnt[0] + acnt[-1])) // 2) * (N - 1)
        ans += ((acnt[0] + 1) * acnt[0]) // 2
        ans += ((acnt[-1] + 1) * acnt[-1]) // 2
    else:
        ans += (((acnt[0] + 1) * acnt[0]) // 2) * N
        ans += (((acnt[-1] + 1) * acnt[-1]) // 2) * N
print(ans)
