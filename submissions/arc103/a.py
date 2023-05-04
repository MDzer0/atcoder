from collections import Counter

n = int(input())
v = list(map(int, input().split()))

tmp = n // 2

tmp1 = []
tmp2 = []

for i in range(n):
    if i % 2 == 0:
        tmp1.append(v[i])
    else:
        tmp2.append(v[i])

tmp1 = Counter(tmp1).most_common(2)
tmp2 = Counter(tmp2).most_common(2)

ans = n

for i in range(len(tmp1)):
    for j in range(len(tmp2)):
        if tmp1[i][0] == tmp2[j][0]:
            continue
        else:
            ans = min(ans, n - tmp1[i][1] - tmp2[j][1])

if ans == n and len(Counter(v)) == 1:
    print(tmp)
else:
    print(ans)
