A, B, C, D = map(int,input().split())
L = A + B
R = C + D
if L > R:
    print('Left')
elif R > L:
    print('Right')
else:
    print('Balanced')
