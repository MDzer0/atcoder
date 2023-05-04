N = int(input())
d, m = divmod(N, 16)
if d == 10:
    d = 'A'
elif d == 11:
    d = 'B'
elif d == 12:
    d = 'C'
elif d == 13:
    d = 'D'
elif d == 14:
    d = 'E'
elif d == 15:
    d = 'F'

if m == 10:
    m = 'A'
elif m == 11:
    m = 'B'
elif m == 12:
    m = 'C'
elif m == 13:
    m = 'D'
elif m == 14:
    m = 'E'
elif m == 15:
    m = 'F'

print(str(d) + str(m))
