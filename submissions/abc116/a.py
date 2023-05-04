abcList = list(map(int, input().split()))
abcList.sort()
ans = int((abcList[0] * abcList[1]) / 2)
print(ans)
