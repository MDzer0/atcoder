import collections
N = int(input())
aLst = list(int(input()) for i in range(N))
ans = collections.Counter(aLst)
tmp = sorted(ans)
print(tmp[-2])
