x, y, w = input().split()
c = [list(input()) for _ in range(9)]
wlist = ['R', 'L', 'U', 'D', 'RU', 'RD', 'LU', 'LD']
ans = ''
x = int(x)
y = int(y)
for i in range(4):
    ans += c[y - 1][x - 1]
    if w == wlist[0]:
        if x == 9:
            x -= 1
            w = wlist[1]
        else:
            x += 1

    elif w == wlist[1]:
        if x == 1:
            x += 1
            w = wlist[0]
        else:
            x -= 1

    elif w == wlist[2]:
        if y == 1:
            y += 1
            w = wlist[3]
        else:
            y -= 1

    elif w == wlist[3]:
        if y == 9:
            y -= 1
            w = wlist[2]
        else:
            y += 1

    elif w == wlist[4]:
        if y == 1 and x == 9:
            x -= 1
            y += 1
            w = wlist[7]
        elif y == 1:
            x += 1
            y += 1
            w = wlist[5]
        elif x == 9:
            x -= 1
            y -= 1
            w = wlist[6]
        else:
            x += 1
            y -= 1

    elif w == wlist[5]:
        if y == 9 and x == 9:
            x -= 1
            y -= 1
            w = wlist[6]
        elif y == 9:
            x += 1
            y -= 1
            w = wlist[4]
        elif x == 9:
            x -= 1
            y += 1
            w = wlist[7]
        else:
            x += 1
            y += 1

    elif w == wlist[6]:
        if y == 1 and x == 1:
            x += 1
            y += 1
            w = wlist[5]
        elif y == 1:
            x -= 1
            y += 1
            w = wlist[7]
        elif x == 1:
            x += 1
            y -= 1
            w = wlist[4]
        else:
            x -= 1
            y -= 1

    elif w == wlist[7]:
        if y == 9 and x == 1:
            x += 1
            y -= 1
            w = wlist[4]
        elif y == 9:
            x -= 1
            y -= 1
            w = wlist[6]
        elif x == 1:
            x += 1
            y += 1
            w = wlist[5]
        else:
            x -= 1
            y += 1

print(ans)
