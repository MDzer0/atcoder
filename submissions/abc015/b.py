import math
N = int(input())
aLst = [int(x) for x in input().split() if x != '0']
ans = math.ceil(sum(aLst) / len(aLst))
print(ans)
