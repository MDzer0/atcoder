from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
abclist = [A, B, C]

ad = defaultdict(int)
bd = defaultdict(int)
cd = defaultdict(int)

for i in range(3):
    for j in abclist[i]:
        if i == 0:
            ad[j % 46] += 1
        elif i == 1:
            bd[j % 46] += 1
        else:
            cd[j % 46] += 1

ans = 0
for i in ad.items():
    for j in bd.items():
        for k in cd.items():
            if (i[0] + j[0] + k[0]) % 46 == 0:
                ans += i[1] * j[1] * k[1]
print(ans)
