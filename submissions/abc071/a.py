x, a, b = map(int, input().split())

tmpa = abs(a - x)
tmpb = abs(b - x)
if tmpa < tmpb:
    print('A')
else:
    print('B')
