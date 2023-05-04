s = list(input())
sets = set(s)

if s.count(list(sets)[0]) == len(s):
    print(0)
    exit()

cnt = 10 ** 9
for i in range(len(sets)):
    find = list(sets)[i]
    tmps = s
    tmpCnt = 0
    while True:
        tmp = ''
        for j in range(len(tmps) - 1, 0, -1):
            if s[j - 1] == find:
                tmp += tmps[j - 1]
            else:
                tmp += tmps[j]
        tmpCnt += 1
        tmps = tmp[::-1]
        if tmps.count(find) == len(tmps):
            cnt = min(cnt, tmpCnt)
            break

print(cnt)
