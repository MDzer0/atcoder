N = int(input())
S = input()

ansMax = 0
ans = 0
for i in range(N):
    if S[i] == 'I':
        ans += 1
    else:
        ans -= 1
    ansMax = max(ansMax, ans)

print(ansMax)
