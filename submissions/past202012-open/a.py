s = input()
m = 0
b = 0

for i in s:
    if i == 'o':
        m += 1
        b = 0
    else:
        b += 1
        m = 0
        
    if m == 3:
        print('o')
        exit()
    elif b == 3:
        print('x')
        exit()
        
print('draw')
