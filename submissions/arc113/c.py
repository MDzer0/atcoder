from collections import defaultdict

S = input()[::-1]
ans = 0
d = defaultdict(int)

for i in range(len(S) - 1):
    if S[i] == S[i + 1]:
        ans += i - d[S[i]]
        d.clear()
        d[S[i]] += i + 1
    else:
        d[S[i]] += 1
print(ans)
