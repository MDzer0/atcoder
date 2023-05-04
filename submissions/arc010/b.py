N = int(input())
l = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = []
for i in range(366):
    if i % 7 == 0 or i % 7 == 6:
        day.append(1)
    else:
        day.append(0)

for i in range(N):
    m, d = map(int, input().split('/'))
    x = sum(l[:m])
    for j in range(x + d - 1, 366):
        if day[j] == 0:
            day[j] = 1
            break

ans = -1
tmp = 0
for i in day:
    if i == 1:
        tmp += 1
    else:
        ans = max(ans, tmp)
        tmp = 0
print(max(ans, tmp))
