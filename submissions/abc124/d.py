import copy
N, K = map(int, input().split())
S = input()
if S.count('0') == 0:
    print(S.count('1'))
    exit()

if N == K:
    print(N)
    exit()

olst = []
zlst = []
tmp = S[0]
tcnt = 1
for i in range(1, N):
    if tmp != S[i]:
        if tmp == '1':
            olst.append(tcnt)
        else:
            zlst.append(tcnt)
        tmp = S[i]
        tcnt = 1
    else:
        tcnt += 1

if tmp == '1':
    olst.append(tcnt)
else:
    zlst.append(tcnt)

index = 0
flst, slst = [], []
if S[0] == '1':
    index = 1
    flst = copy.deepcopy(olst)
    slst = copy.deepcopy(zlst)
else:
    flst = copy.deepcopy(zlst)
    slst = copy.deepcopy(olst)
total = [0] * (len(flst) + len(slst) + 1)
for i in range(1, len(flst) + len(slst) + 1):
    if i % 2 != 0:
        total[i] += flst[i // 2] + total[i - 1]
    else:
        total[i] += slst[i // 2 - 1] + total[i - 1]
ans = 0
tmp1 = (2 * K) - 1
tmp2 = 2 * K
for i in range(1, len(total) - K):
    tmp = 0
    if index == 0:
        if i % 2 != 0:
            if i + tmp1 < len(total):
                tmp += total[i + tmp1] - total[i - 1]
            else:
                tmp += total[-1] - total[i - 1]
        else:
            if i + tmp2 < len(total):
                tmp += total[i + tmp2] - total[i - 1]
            else:
                tmp += total[-1] - total[i - 1]
    else:
        if i % 2 != 0:
            if i + tmp2 < len(total):
                tmp += total[i + tmp2] - total[i - 1]
            else:
                tmp += total[-1] - total[i - 1]
        else:
            if i + tmp1 < len(total):
                tmp += total[i + tmp1] - total[i - 1]
            else:
                tmp += total[-1] - total[i - 1]
    ans = max(ans, tmp)
print(ans)
