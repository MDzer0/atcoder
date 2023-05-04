N = int(input())
a = list(map(int, input().split()))
slst = []
llst = []
stmp = 201
ltmp = 0
for i in a:
    if stmp >= i:
        stmp = i
    else:
        slst.append(stmp)
        stmp = i

for i in reversed(a):
    if ltmp <= i:
        ltmp = i
    else:
        llst.insert(0, ltmp)
        ltmp = i

total = 1000
for i in range(len(slst)):
    cnt = total // slst[i]
    total -= (slst[i] * cnt)
    total += (llst[i] * cnt)

print(total)
