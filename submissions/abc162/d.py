N = int(input())
S = input()
rcnt = S.count('R')
gcnt = S.count('G')
bcnt = S.count('B')
ans = rcnt * gcnt * bcnt

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        if S[i] == S[j]:
            continue
        if j + (j - i) >= N:
            break
        if S[i] != S[j] and S[j] != S[j + (j - i)] and S[i] != S[j + (j - i)]:
            ans -= 1
print(ans)
