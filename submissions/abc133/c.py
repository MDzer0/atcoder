import sys

inf = 2019
L, R = map(int, input().split())

if (R - L) >= 2019:
    print(0)
    sys.exit()

ans = 2019
   
for i in range(L, R):

    for j in range(i + 1, R + 1):
        tmp = int((i * j) % inf)
        ans = min(ans, tmp)
        if ans == 0:
            break
    if ans == 0:
        break

print(ans)
