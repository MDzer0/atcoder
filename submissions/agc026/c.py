from collections import defaultdict

N = int(input())
S = input()
lS = S[:N]
rS = S[N:][::-1]
left = defaultdict(int)
right = defaultdict(int)

for i in range(1 << N):
    r, b = '', ''
    for j in range(N):
        if i >> j & 1:
            r += lS[j]
        else:
            b += lS[j]
    left[(r, b)] += 1

for i in range(1 << N):
    r, b = '', ''
    for j in range(N):
        if i >> j & 1:
            r += rS[j]
        else:
            b += rS[j]
    right[(r, b)] += 1

ans = 0
for i in left.keys():
    ans += left[i] * right[i]

print(ans)
