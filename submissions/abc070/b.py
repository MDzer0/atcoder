A, B, C, D = map(int, input().split())

if B < D:
    if A < C:
        frst = B - C
    else:
        frst = B - A
else:
    if A < C:
        frst = D - C
    else:
        frst = D - A
    
if frst <= 0:
    print(0)
else:
    print(frst)
