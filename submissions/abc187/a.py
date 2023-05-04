A, B = input().split()
tmpA = 0
tmpB = 0

for i in A:
    tmpA += int(i)

for i in B:
    tmpB += int(i)

if tmpA >= tmpB:
    print(tmpA)
else:
    print(tmpB)
