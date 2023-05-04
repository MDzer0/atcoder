N, X = map(int, input().split())
S = input()
T = [int(input()) for _ in range(N)]
ans = 0
for i in range(N):
    if S[i] == '1':
        ans += min(X, T[i])
    else:
        ans += T[i]

print(ans)
