L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

tmp = 0
a1, a2 = divmod(A, C)
if a2 != 0:
    tmp = a1 + 1
else:
    tmp = a1

b1, b2 = divmod(B, D)
if b2 != 0:
    tmp = max(tmp, b1 + 1)
else:
    tmp = max(tmp, b1)


print(L - tmp)
