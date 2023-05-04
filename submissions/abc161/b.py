N, M = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
total = sum(a)
tmp = 1 / (4 * M)
cnt = 0
for i in a:
    if i >= total * tmp:
        cnt += 1
    else:
        break
if cnt >= M:
    print('Yes')
else:
    print('No')
