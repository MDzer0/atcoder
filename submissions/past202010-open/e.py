from collections import defaultdict

N = int(input())
S = input()
d = defaultdict(int)

for i in S:
    d[i] += 1

if len(d) == 1 or N == 2:
    print('None')
    exit()

for i in range(N):
    ans = ''
    for j in range(i, N + i):
        ans += S[j % N]
    if ans != S and ans != S[::-1]:
        print(ans)
        exit()

ans = ''
for v, d in d.items():
    ans += v * d
print(ans)
