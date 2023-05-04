from collections import defaultdict

N, K, C = map(int, input().split())
s = list(input())
llst = []
rlst = []

index = 0
lcnt = 0
while index < N:
    if s[index] == 'o':
        llst.append(index)
        index += C + 1
        lcnt += 1
        if lcnt == K:
            break
    else:
        index += 1
index = N - 1
rcnt = 0
while index >= 0:
    if s[index] == 'o':
        rlst.append(index)
        index -= (C + 1)
        rcnt += 1
        if rcnt == K:
            break
    else:
        index -= 1

ans = []
for i in range(len(llst)):
    if i <= len(rlst):
        if llst[i] == rlst[-i - 1]:
            ans.append(llst[i] + 1)
    else:
        break

for i in ans:
    print(i)
