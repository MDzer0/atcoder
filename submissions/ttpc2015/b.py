N, B, C = map(int, input().split())
if B == 0 or C == 0:
    print(0)
    exit()
if B > C:
    B = C
m, d = divmod(C, B)
a = list(map(int, input().split()))
mcnt = 0
dcnt = 0
ans = 0
a.sort(reverse=True)
for i in a:
    if mcnt < m:
        ans += i * B
        mcnt += 1
    elif dcnt == 0:
        ans += i * d
        dcnt += 1
    else:
        break
print(ans)
