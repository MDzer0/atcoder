from collections import defaultdict

N = int(input())
cnt = defaultdict(int)

for i in range(1, N + 1):
    h = str(i)[0]
    f = str(i)[-1]
    if f == '0':
        continue
    cnt[(h, f)] += 1

ans = 0
dlst = list(cnt.items())
for i, v in dlst:
    ans += v * cnt[i[1], i[0]]

print(ans)
