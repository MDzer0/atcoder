N, M = map(int, input().split())
S = input()

if S[0] == 'R':
    tmp = 'RL'
else:
    tmp = 'LR'
cnt = 0
ans = 0
for i in range(len(S) - 1):
    if S[i] == S[i + 1]:
        ans += 1
    if S[i:i + 2] == tmp:
        cnt += 1

if cnt > M:
    ans += 2 * M
else:
    ans += 2 * cnt

if N == ans:
    ans -= 1
print(ans)
