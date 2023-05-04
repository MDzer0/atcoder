N = int(input())
alist = '123456'
tmp =  N // 5
tmp = tmp % 6
amari = N % 5
alist = alist[tmp:] + alist[0:tmp]
for i in range(amari):
    alist = alist[0:i] + alist[i + 1] + alist[i] + alist[i + 2:]
print(alist)
