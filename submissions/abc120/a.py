A, B, C = map(int, input().split())
tmpA = B // A
if tmpA > C:
    print(C)
else:
    print(tmpA)
