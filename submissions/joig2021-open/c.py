N = int(input())
A = list(map(int, input().split()))
tmpA = [0] * N
r = -1
cnt = 0
tmp = 0

for i in range(N):
    if A[i] == 1:
        cnt += 1
    else:
        cnt -= 1
    if cnt > tmp:
        r = i
        tmp = cnt

if r >= 0:
    for i in range(r + 1):
        tmpA[i] = 1

ans = 0
for i in range(N):
    if A[i] != tmpA[i]:
        ans += 1

print(ans)
