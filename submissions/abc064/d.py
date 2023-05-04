N = int(input())
S = input()
tmp = S[-1]
index = 0
ans = ''
cnt1 = 0
cnt2 = 0
for i in range(N):
    if S[i] == '(':
        cnt1 += 1
    elif cnt1 == 0:
        cnt2 += 1
    else:
        cnt1 -= 1

print('(' * cnt2 + S + ')' * cnt1)
