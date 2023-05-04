N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
S = 0
cnt = 0
for i in range(N):
    if a[i] < b[i]:
        S += (b[i] - a[i])
        cnt += 1
if S == 0:
    print(0)
    exit()
T = 0
sumlst = []
for i in range(N):
    if a[i] >= b[i]:
        sumlst.append(a[i] - b[i])

sumlst.sort(reverse=True)
for i in sumlst:
    T += i
    cnt += 1
    if T >= S:
        break
if S > T:
    print(-1)
    exit()
print(cnt)
