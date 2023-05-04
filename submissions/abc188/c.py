N = int(input())
a = list(map(int, input().split()))
lmax = max(a[:((2 ** N) // 2)])
rmax = max(a[(2 ** N) // 2:])
if lmax > rmax:
    print(a.index(rmax) + 1)
else:
    print(a.index(lmax) + 1)
