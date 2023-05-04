N = int(input())
a = list(map(int, input().split()))
cnt = 0
zcnt = a.count(0)
for i in range(N):
    if a[i] < 0:
        cnt += 1

total = 0
if cnt % 2 == 0 or (cnt % 2 != 0 and zcnt > 0):
    for i in range(N):
        total += abs(a[i])
else:
    tmp = 10 ** 9
    for i in range(N):
        total += abs(a[i])
        tmp = min(tmp, abs(a[i]))
    total -= 2 * tmp

print(total)
