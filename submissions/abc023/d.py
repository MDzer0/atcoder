N = int(input())
hs = [list(map(int, input().split())) for _ in range(N)]

hi = 10 ** 15
low = 0
while hi - low > 1:
    mid = (hi + low) // 2
    hslist = []
    for i in hs:
        hslist.append((mid - i[0]) // i[1])
    hslist.sort()
    bflag = True
    for i in range(N):
        if hslist[i] < i:
            bflag = False
            break

    if bflag:
        hi = mid
    else:
        low = mid

print(hi)
