N = int(input())
S = input()
ans = ''
for i in range(1, N):
    if S[i - 1] != S[i]:
        ans += S[i - 1]

if ans == '' or (ans[-1] != S[-1]):
    ans += S[-1]

print(len(ans))
