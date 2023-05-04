N = int(input())
gcdlst = []
for i in range(1, int(N ** 0.5) + 1):
    if N % i == 0:
        gcdlst.append(i)
        if i != N // i:
            gcdlst.append(N // i)
gcdlst.sort()
tmplen = len(gcdlst)
if tmplen % 2 == 0:
    tmplen = tmplen // 2
    ans = gcdlst[tmplen] + gcdlst[tmplen - 1] - 2
else:
    tmplen = tmplen // 2
    ans = (2 * gcdlst[tmplen]) - 2
print(ans)
