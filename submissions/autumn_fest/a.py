N, T = map(int, input().split())
P = list(map(int, input().split()))
scoa = [list(map(int, input().split())) for _ in range(N)]
time = [list(map(int, input().split())) for _ in range(N)]
timescoa = []

for i in range(N):
    for j in range(len(scoa[i])):
        tmp = []
        tmp.append(scoa[i][j])
        tmp.append(i)
        tmp.append(time[i][j])
        if j != 0: tmp.append(scoa[i][j - 1])
        timescoa.append(tmp)
timescoa.sort(key=lambda x: x[1])
timescoa.sort()

ans = 0
time = 0
for i in timescoa:
    time += i[2]
    if time > T: break
    ans += i[0]
    if len(i) == 4:
        ans -= i[3]

print(ans)
