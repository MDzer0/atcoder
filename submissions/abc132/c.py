import bisect

N = int(input())
dlist = list(map(int, input().split()))

dlist.sort()

inta = dlist[(N // 2) - 1]
intb = dlist[(N // 2)]

ans = intb - inta
print(ans)
