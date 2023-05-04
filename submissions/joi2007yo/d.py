n = int(input())
nlst = [i for i in range(1, 2 * n + 1)]
m = int(input())
for i in range(m):
    A = []
    B = []
    tmp = int(input())
    if tmp == 0:
        A = nlst[:n]
        B = nlst[n:]
        nlst = []
        for j in range(n):
            nlst.append(A[j])
            nlst.append(B[j])
    else:
        A = nlst[:tmp]
        B = nlst[tmp:]
        nlst = B + A

for i in nlst:
    print(i)
