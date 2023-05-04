N = int(input())
c = list(map(int, input().split()))
kisuc = []
for i in range(0, N, 2):
    kisuc.append(c[i])
Q = int(input())
mintotal = min(c)
minkisu = min(kisuc)
totalcnt = 0
kisucnt = 0
cnt = 0

for i in range(Q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        if s[1] % 2 == 0 and c[s[1] - 1] - s[2] - totalcnt >= 0:
            c[s[1] - 1] -= s[2]
            cnt += s[2]
            mintotal = min(mintotal, c[s[1] - 1])
        elif s[1] % 2 != 0 and c[s[1] - 1] - s[2] - totalcnt - kisucnt >= 0:
            c[s[1] - 1] -= s[2]
            cnt += s[2]
            mintotal = min(mintotal, c[s[1] - 1])
            minkisu = min(minkisu, c[s[1] - 1])
    elif s[0] == 2:
        if minkisu - s[1] >= 0:
            cnt += len(kisuc) * s[1]
            kisucnt += s[1]
            minkisu -= s[1]
    else:
        if min(minkisu - s[1], mintotal - s[1]) >= 0:
            cnt += N * s[1]
            totalcnt += s[1]
            mintotal -= s[1]
            minkisu -= s[1]
print(cnt)
