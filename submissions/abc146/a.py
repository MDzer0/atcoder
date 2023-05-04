S = input()
slst = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
tmp = slst.index(S) + 1
if 7 == tmp:
    print(7)
else:
    print(7 - tmp)
