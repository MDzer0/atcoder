N = int(input())
a = list(map(int, input().split()))

cnt = N
tmplst = []
tmp = 1
for i in range(1, N):
    if a[i - 1] < a[i]:
        tmp += 1
    else:
        if tmp > 1:
            tmplst.append(tmp)
            tmp = 1
if tmp > 1:
    tmplst.append(tmp)
for i in tmplst:
    cnt += (i * (i - 1)) // 2
print(cnt)
