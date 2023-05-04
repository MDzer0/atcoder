okaneLst = list(map(str, input().split()))
okaneLst.sort(reverse=True)
ab = int(okaneLst[0] + okaneLst[1])
print(ab + int(okaneLst[2]))
