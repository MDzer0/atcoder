a = input()
b = input()
c = input()

ans = ''
next = a[0]
a = a[1:]
for i in range(len(a) + len(b) + len(c)):
    if next == 'a':
        if len(a) == 0:
            ans = 'A'
            break
        next = a[0]
        a = a[1:]
    if next == 'b':
        if len(b) == 0:
            ans = 'B'
            break
        next = b[0]
        b = b[1:]

    if next == 'c':
        if len(c) == 0:
            ans = 'C'
            break
        next = c[0]
        c = c[1:]

print(ans)
