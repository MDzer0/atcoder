def createList(n, flg):
    for i in range(1, n + 1):
        if flg == 0:
            alist.append(i)
        else:
            blist.append(-i)
A, B = map(int, input().split())
alist = []
blist = []

createList(A, 0)
createList(B, 1)

sumjuge = sum(alist) - abs(sum(blist))
if sumjuge > 0:
    blist[-1] -= sumjuge
elif sumjuge < 0:
    alist[-1] += abs(sumjuge)

print(*(alist + blist))
