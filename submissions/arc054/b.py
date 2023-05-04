P = float(input())

def f(p, x):
    return x + p / (pow(2, x / 1.5))

e = 10**-9
high = 100
low = 0
while high - low > e:
    tmp1 = high / 3 + low * 2 / 3
    tmp2 = high * 2 / 3 + low / 3
    if f(P, tmp2) < f(P, tmp1):
        low = tmp1
    else:
        high = tmp2

print(f(P, high))
