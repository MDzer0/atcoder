A, B = map(int, input().split())
tmpa = abs(A)
tmpb = abs(B)

if tmpa == tmpb:
    print('Draw')
elif tmpa > tmpb:
    print('Bug')
else:
    print('Ant')
