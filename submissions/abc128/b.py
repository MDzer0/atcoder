from collections import defaultdict
N = int(input())
alst = []
slst = defaultdict(list)
for i in range(N):
    k, v = map(str, input().split())
    slst[k].append(v)
    alst.append(k + ',' + v)

tmp = sorted(slst)
xlst = []
for i in tmp:
    x = slst[i]
    xx = []
    for j in x:
        xx.append(int(j))
    xtmp = sorted(xx, reverse=True)
    for j in xtmp:
        xlst.append(i + ',' + str(j))

anslst = [0] * N
anstmp = 0
for i in xlst:
    for j in range(len(alst)):
        if alst[j] == i:
            anslst[anstmp] = j + 1
            anstmp += 1
            break

for i in anslst:
    print(i)
