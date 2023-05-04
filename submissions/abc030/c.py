import bisect

N, M = map(int, input().split())
X, Y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt = 0
tmpa = a[0] + X
tmpb = 0
while True:
    if tmpa != 0:
        tmp = bisect.bisect_left(b, tmpa)
        if tmp == len(b):
            break
        else:
            tmpb = b[tmp] + Y
            tmpa = 0
            cnt += 1
    else:
        tmp = bisect.bisect_left(a, tmpb)
        if tmp == len(a):
            break
        else:
            tmpa = a[tmp] + X
            tmpb = 0

print(cnt)
